import nfldpw
import requests
import pandas
import nfldpw.drafts
import nfldpw.pbp
import nfldpw.players
import nfldpw.rosters
import nfldpw.schedules
import io
import numpy


CACHE = "cache/"


PBP_DICT = "https://nflreadr.nflverse.com/articles/dictionary_pbp.html"
NGS_DICT = "https://nflreadr.nflverse.com/articles/dictionary_nextgen_stats.html"
PARTICIPATION_DICT = (
    "https://nflreadr.nflverse.com/articles/dictionary_participation.html"
)
SCHEDULES_DICT = "https://nflreadr.nflverse.com/articles/dictionary_schedules.html"
ROSTERS_DICT = "https://nflreadr.nflverse.com/articles/dictionary_rosters.html"
PLAYER_STATS_DICT = (
    "https://nflreadr.nflverse.com/articles/dictionary_player_stats.html"
)
PLAYERS_DICT = "https://nflreadr.nflverse.com/articles/dictionary_ff_playerids.html"
DRAFTS_DICT = "https://nflreadr.nflverse.com/articles/dictionary_draft_picks.html"

PBP_URLS = [PBP_DICT, NGS_DICT, PARTICIPATION_DICT]
SCHEDULES_URLS = [SCHEDULES_DICT]
ROSTERS_URLS = [ROSTERS_DICT, PLAYER_STATS_DICT]
PLAYERS_URLS = [PLAYERS_DICT, ROSTERS_DICT, PLAYER_STATS_DICT]
DRAFTS_URLS = [DRAFTS_DICT, PLAYERS_DICT, ROSTERS_DICT]


def get_nflverse_dict(url: str) -> list[list[str]]:
    text = requests.get(url).text
    ind1 = text.find("[[")
    ind2 = text.find("]]")
    table = None
    if ind1 == -1 or ind2 == -1:
        df = pandas.read_html(io.StringIO(text))[0]
        table = df.T.values.tolist()
    else:
        table = eval(text[ind1 : ind2 + 2])
    if (
        table[1][0] == "character"
        or table[1][0] == "numeric"
        or table[1][0] == "integer"
    ):
        t1 = table[1]
        table[1] = table[2]
        table[2] = t1
    return table


def format_col(col: str) -> str:
    new_col = ""
    first = True
    for i in range(0, len(col)):
        if first:
            new_col += col[i].upper()
            first = False
        elif col[i] == "_":
            first = True
        else:
            new_col += col[i]
    return new_col


UNFOUND_DOCSTINGS = {
    "football_name": "Player's displayed football name.",
    "entry_year": "Player's first year rostered on an NFL team.",
    "rookie_year": "Player's rookie year.",
    "draft_club": "NFL team that drafted the player (if applicable).",
    "draft_number": "Player's draft number.",
    "age": "Player's current age",
    "display_name": "Player's displayed football name.",
    "college_name": "Player's college.",
    "college_conference": "Player's college conference.",
}


def tables_find(tables: list[list[list[str]]], col: str) -> str:
    for table in tables:
        for i in range(0, len(table[0])):
            if table[0][i] == col:
                return table[1][i]
    for key in UNFOUND_DOCSTINGS:
        if col == key:
            return UNFOUND_DOCSTINGS[key]
    print("FAILED TO FIND COLUMN:", col)
    return "No documentation available."


def format_value(value: str) -> str:
    new_value = ""
    for char in value:
        if char != "'" and char != "." and char != "-":
            if char == " ":
                new_value += "_"
            else:
                new_value += char
    return new_value


UNIQUE_NUM = 100

PBP_NOT_KEEP = [
    "desc",
    "game_id",
    "play_id",
    "old_game_id_x",
    "game_date",
    "start_time",
    "nfl_api_id",
    "time",
    "time_of_day",
    "offense_personnel",
    "defense_personnel",
    "players_on_play",
    "offense_players",
    "defense_players",
    "weather",
    "receiver",
    "rusher",
    "passer",
    "drive_start_yard_line",
    "yrdln",
    "drive_end_yard_line",
    "fantasy",
    "gameday",
    "pfr",
    "headshot_url",
    "draft_club",
    "birth_date",
    "headshot",
    "years_of_experience",
    "uniform_number",
    "draft_round",
]


def values_binary(values: list) -> bool:
    if (len(values) == 2 or len(values) == 3) and (
        (1 in values or 1.0 in values) and (0 in values or 0.0 in values)
    ):
        return True
    else:
        return False


def values_string(values: list) -> bool:
    for value in values:
        if not isinstance(value, str):
            return False
    return True


def col_values(df: pandas.DataFrame, col: str) -> list[str]:
    if (
        col not in PBP_NOT_KEEP
        and "id" not in col
        and "name" not in col
        and "time" not in col
        and "coach" not in col
        and "clock" not in col
        and "team" not in col
    ):
        values = list(df[col].unique())
        if "nan" in values:
            values.remove("nan")
        if "None" in values:
            values.remove("None")
        if "" in values:
            values.remove("")
        if None in values:
            values.remove(None)
        if len(values) > 0:
            lines = [""]
            if values_binary(values):
                lines.append("\tTRUE = 1")
                lines.append("\tFALSE = 0")
                return lines
            elif values_string(values):
                for value in values:
                    string = value.replace("2_MAN", "MAN_2")
                    string = string.replace("&amp;", "AND")
                    string = string.replace("(", "")
                    string = string.replace(")", "")
                    string = string.replace(";", "")
                    string = string.replace(" < ", "_")
                    string = string.replace(" ", "_")
                    string = string.replace(".", "")
                    string = string.replace("-", "")
                    string = string.replace("'", "")
                    string = string.replace("&", "")
                    string = string.replace("®", "")
                    string = string.replace("/", "")
                    string = string.replace(",", "")
                    string = string.upper()
                    lines.append("\t" + string + ' = "' + value + '"')
                return lines
    return []


NUM_EXAMPLE_VALUES = 5


def example_values(df: pandas.DataFrame, col: str) -> list[str]:
    lines = []
    lines.append("")
    lines.append("\tExample Values")
    lines.append("\t--------------")
    lines.append("")
    for i in range(0, NUM_EXAMPLE_VALUES):
        value = df[col].iloc[i]
        if (
            isinstance(value, int)
            or isinstance(value, float)
            or isinstance(value, numpy.float32)
            or isinstance(value, numpy.float64)
        ):
            lines.append("\t`" + str(value) + "`")
        else:
            lines.append('\t`"' + str(value) + '"`')
        lines.append("")
    return lines


def pbp_col(df: pandas.DataFrame, col: str, tables: list[list[list[str]]]) -> list[str]:
    lines = []
    lines.append("class " + format_col(col) + ":")
    lines.append('\t"""')
    lines.append("\t" + tables_find(tables, col))
    lines += example_values(df, col)
    lines.append('\t"""')
    lines.append("")
    lines.append('\theader = "' + col + '"')
    lines += col_values(df, col)
    return lines


def lines_write(lines: list[str], path: str):
    string = ""
    for line in lines:
        string += line + "\n"
    with open(path, "w") as file:
        file.write(string)


def pbp():
    tables = []
    for url in PBP_URLS:
        tables.append(get_nflverse_dict(url))
    df = nfldpw.pbp.get([2023], CACHE)
    lines = []
    for col in df.columns:
        lines += pbp_col(df, col, tables)
        lines.append("")
    file_path = "nfldpw/pbp/cols.py"
    lines_write(lines, file_path)


def schedules_col(
    df: pandas.DataFrame, col: str, tables: list[list[list[str]]]
) -> list[str]:
    lines = []
    lines.append("class " + format_col(col) + ":")
    lines.append('\t"""')
    lines.append("\t" + tables_find(tables, col))
    lines += example_values(df, col)
    lines.append('\t"""')
    lines.append("")
    lines.append('\theader = "' + col + '"')
    lines += col_values(df, col)
    return lines


def schedules():
    tables = []
    for url in SCHEDULES_URLS:
        tables.append(get_nflverse_dict(url))
    df = nfldpw.schedules.get([2023], CACHE)
    lines = []
    for col in df.columns:
        lines += schedules_col(df, col, tables)
        lines.append("")
    file_path = "nfldpw/schedules/cols.py"
    lines_write(lines, file_path)


def rosters_col(
    df: pandas.DataFrame, col: str, tables: list[list[list[str]]]
) -> list[str]:
    lines = []
    lines.append("class " + format_col(col) + ":")
    lines.append('\t"""')
    lines.append("\t" + tables_find(tables, col))
    lines += example_values(df, col)
    lines.append('\t"""')
    lines.append("")
    lines.append('\theader = "' + col + '"')
    lines += col_values(df, col)
    return lines


def rosters():
    tables = []
    for url in ROSTERS_URLS:
        tables.append(get_nflverse_dict(url))
    df = nfldpw.rosters.get([2023], CACHE)
    lines = []
    for col in df.columns:
        lines += rosters_col(df, col, tables)
        lines.append("")
    file_path = "nfldpw/rosters/cols.py"
    lines_write(lines, file_path)


def players_col(
    df: pandas.DataFrame, col: str, tables: list[list[list[str]]]
) -> list[str]:
    lines = []
    lines.append("class " + format_col(col) + ":")
    lines.append('\t"""')
    lines.append("\t" + tables_find(tables, col))
    lines += example_values(df, col)
    lines.append('\t"""')
    lines.append("")
    lines.append('\theader = "' + col + '"')
    lines += col_values(df, col)
    return lines


def players():
    tables = []
    for url in PLAYERS_URLS:
        tables.append(get_nflverse_dict(url))
    df = nfldpw.players.get(CACHE)
    lines = []
    for col in df.columns:
        lines += players_col(df, col, tables)
        lines.append("")
    file_path = "nfldpw/players/cols.py"
    lines_write(lines, file_path)


def drafts_col(
    df: pandas.DataFrame, col: str, tables: list[list[list[str]]]
) -> list[str]:
    lines = []
    lines.append("class " + format_col(col) + ":")
    lines.append('\t"""')
    lines.append("\t" + tables_find(tables, col))
    lines += example_values(df, col)
    lines.append('\t"""')
    lines.append("")
    lines.append('\theader = "' + col + '"')
    lines += col_values(df, col)
    return lines


def drafts():
    tables = []
    for url in DRAFTS_URLS:
        tables.append(get_nflverse_dict(url))
    df = nfldpw.drafts.get([2023], CACHE)
    lines = []
    for col in df.columns:
        lines += drafts_col(df, col, tables)
        lines.append("")
    file_path = "nfldpw/drafts/cols.py"
    lines_write(lines, file_path)


drafts()
