import nfldpw
import requests
import pandas
import nfldpw.pbp
import io
import numpy


CACHE = "cache/"


PBP_DICT = "https://nflreadr.nflverse.com/articles/dictionary_pbp.html"
NGS_DICT = "https://nflreadr.nflverse.com/articles/dictionary_nextgen_stats.html"
PARTICIPATION_DICT = (
    "https://nflreadr.nflverse.com/articles/dictionary_participation.html"
)

PBP_URLS = [PBP_DICT, NGS_DICT, PARTICIPATION_DICT]


def get_nflverse_dict(url: str) -> list[list[str]]:
    text = requests.get(url).text
    ind1 = text.find("[[")
    ind2 = text.find("]]")
    table = None
    if ind1 == -1 or ind2 == -1:
        df = pandas.read_html(io.StringIO(text))[0]
        table = df.T.values.tolist()
        t1 = table[1]
        table[1] = table[2]
        table[2] = t1
    else:
        table = eval(text[ind1 : ind2 + 2])
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


def tables_find(tables: list[list[list[str]]], col: str) -> str:
    for table in tables:
        for i in range(0, len(table[0])):
            if table[0][i] == col:
                return table[1][i]
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
            lines.append("\tclass values:")
            if values_binary(values):
                lines.append("\t\tTRUE = 1")
                lines.append("\t\tFALSE = 0")
                return lines
            elif values_string(values):
                for value in values:
                    string = value.replace("2_MAN", "MAN_2")
                    string = string.replace(" ", "_")
                    string = string.replace(".", "")
                    string = string.replace("-", "")
                    string = string.replace("'", "")
                    string = string.replace("&", "")
                    string = string.replace("®", "")
                    string = string.replace("/", "")
                    string = string.replace(",", "")
                    string = string.upper()
                    lines.append("\t\t" + string + ' = "' + value + '"')
                return lines
    return []


def pbp_col(df: pandas.DataFrame, col: str, tables: list[list[list[str]]]) -> list[str]:
    lines = []
    lines.append("class " + format_col(col) + ":")
    lines.append('\t"""')
    lines.append("\t" + tables_find(tables, col))
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


pbp()
