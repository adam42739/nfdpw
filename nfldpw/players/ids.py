import pandas
import os
import nfl_data_py
from .. import cache
from .. import players
from .. import drafts
from .. import rosters
from ..drafts import EXTRA_DRAFT_ID
import tqdm
import datetime


YAHOO = "yahoo_id"
ESB = "esb_id"
SMART = "smart_id"
NFL = "nfl_id"
ESPN = "espn_id"
ROTOWORLD = "rotoworld_id"
GSIS = "gsis_id"
SLEEPER = "sleeper_id"
STATS = "stats_id"
SPORTRADAR = "sportradar_id"
CBS = "cbs_id"
STATS_GLOBAL = "stats_global_id"
CFBREF = "cfbref_id"
FLEAFLICKER = "fleaflicker_id"
FANTASYPROS = "fantasypros_id"
FANTASY_DATA = "fantasy_data_id"
PFF = "pff_id"
MFL = "mfl_id"
PFR = "pfr_id"
ROTOWIRE = "rotowire_id"
KTC = "ktc_id"
SWISH = "swish_id"

DTYPE_LIST = {
    YAHOO: "float64",
    ESB: "object",
    SMART: "object",
    NFL: "object",
    ESPN: "float64",
    ROTOWORLD: "float64",
    GSIS: "object",
    SLEEPER: "float64",
    STATS: "float64",
    SPORTRADAR: "object",
    CBS: "float64",
    STATS_GLOBAL: "float64",
    CFBREF: "object",
    FLEAFLICKER: "float64",
    FANTASYPROS: "float64",
    FANTASY_DATA: "float64",
    PFF: "float64",
    MFL: "float64",
    PFR: "object",
    ROTOWIRE: "float64",
    KTC: "float64",
    SWISH: "float64",
    EXTRA_DRAFT_ID: "object",
}


def current_season() -> int:
    today = datetime.datetime.today()
    if today.month <= 3:
        return today.year - 1
    else:
        return today.year


def get_mapping(cache_path: str = None, refresh: bool = False) -> pandas.DataFrame:
    """
    Load the player ID map. If a cache path is provided `get_mapping` will check to see if a mapping file already exists,
    if it does not it will store the mapping in the cache.

    Parameters
    ----------

    cache_path : str = None
        Directory to get/store the mapping.

    refresh : bool = False
        Whether to refresh the mapping stored in cache.

    Returns
    -------

    out : pandas.DataFrame
        Player ID map.
    """
    if cache_path:
        path = cache_path + cache.fname_players() + "-idraw.csv"
        if os.path.exists(path) and refresh == False:
            return pandas.read_csv(path)
        else:
            df = nfl_data_py.import_ids()
            df.to_csv(path)
            return df
    else:
        return nfl_data_py.import_ids()


def locate_map(id_map: pandas.DataFrame, id_dict: dict[str, str]) -> pandas.Series:
    """
    Locates the row in `id_map` matching the player IDs given in `id_dict`. All IDs present
    in both `id_map` and `id_dict` must be equal to be considered "matching". If no match is found,
    and empty `pandas.Series(dtype="string")` is returned.

    Parameters
    ----------

    id_map : pandas.DataFrame
        Table of IDs where each row is a player and column a type of ID. `None`/`NaN` may exist.

    id_dict : dict[str, str]
        Dictionary of IDs for a single player to match with the `id_map`. Key = ID type; Value = ID

    Returns
    -------

    out : pandas.Series
        Matching player series from the `id_map` or an empty series if no match was found.
    """
    for id in id_dict:
        if id in id_map.columns:
            mask = id_map[id] == id_dict[id]
            df = id_map[mask]
            if len(df) > 0:
                series = df.iloc[0]
                series_compare = pandas.Series(id_dict)
                common = series.index.intersection(series_compare.index)
                same = all(series[common] == series_compare[common])
                if same:
                    return series
    return pandas.Series(dtype="string")


class IDKeeper:
    """
    Class for keeping track of player IDs. An instance of `IDKeeper` is associated with a single cache directory which
    is set by the `IDKeeper.load()` method.
    """

    def __init__(self):
        pass

    def _path(self, cache_path: str) -> str:
        return cache_path + cache.fname_players() + "-idkeeper.csv"

    def load(self, cache_path: str):
        """
        Load the `IDKeeper` from the given cache directory or create one if it does not exist.

        Parameters
        ----------

        cache_path : str
            Cache directory location
        """
        self.cache_path = cache_path
        path = self._path(cache_path)
        self.df = pandas.DataFrame({id_header: [] for id_header in DTYPE_LIST})
        if os.path.exists(path):
            self.df = pandas.concat([self.df, pandas.read_csv(path, index_col=0)])

    def dump(self):
        """
        Save the `IDKeeper` to associated cach direcotry.
        """
        path = self._path(self.cache_path)
        self.df.to_csv(path, index=True)

    def exists(self, id_dict: dict[str, str]) -> bool:
        """
        Check if the player assocated with the IDs in `id_dict` exists in the `IDKeeper`. Only
        one id from `id_dict` must exist in the `IDKeeper` to be considered existing.

        Parameters
        ----------

        id_dict : dict[str, str]
            IDs to check existance in the `IDKeeper`. Key = ID type; Value = ID

        Returns
        -------

        out : bool
            Whether the player exists in the `IDKeeper`
        """
        for id in id_dict:
            if id_dict[id] in self.df[id].values:
                return True
        return False

    def append(self, id_dict: dict[str, str]):
        """
        Append the player given by the IDs in `id_dict` to the keeper. If at least one ID already exists in `IDKeeper`
        nothing is done.

        Parameters
        ----------

        id_dict : dict[str, str]
            IDs to append to the `IDKeeper`. Key = ID type; Value = ID
        """
        if not self.exists(id_dict):
            row = {id: None for id in DTYPE_LIST}
            for id in id_dict:
                row[id] = id_dict[id]
            self.df.loc[len(self)] = row

    def _update_mapping(self, id_map: pandas.DataFrame, part_i: int, part_total: int):
        """
        Updates a single mapping given by `id_map` as opposed to all the mappings which is performed by `IDKeeper.update_mapping()`
        """
        for index in tqdm.tqdm(
            iterable=self.df.index,
            desc="Updating map part: " + str(part_i) + " of " + str(part_total),
            total=len(self.df),
        ):
            id_dict = self.df.iloc[index].dropna().to_dict()
            series = locate_map(id_map, id_dict)
            if not series.empty:
                series_dict = series.to_dict()
                for id in series_dict:
                    self.df.at[index, id] = series_dict[id]

    def update_mapping(self, update_map: bool = False):
        """
        Update the ID mappings in the `IDKeeper` by referencing the mapping (`ids.get_mapping()`) and the
        players `DataFrame` (`players.get()`).

        Parameters
        ----------

        update_map : bool = False
            Whether the refence mapping should be updated. Set to `True` when updating advancing a week for example.
        """
        id_map = get_mapping(self.cache_path, update_map)
        id_list = []
        for id in DTYPE_LIST:
            if id in id_map.columns:
                id_list.append(id)
        id_map = id_map[id_list]
        player_map = players.get(self.cache_path, update_map)
        player_map = player_map[
            [
                players.cols.EsbId.header,
                players.cols.GsisId.header,
                players.cols.SmartId.header,
                EXTRA_DRAFT_ID,
            ]
        ]
        self._update_mapping(id_map, 1, 3)
        self._update_mapping(player_map, 2, 3)
        self._update_mapping(id_map, 3, 3)

    def add_drafts(self, seasons: list[int]):
        """
        Add all drafted players from the given seasons to the `IDKeeper`, update the mapping, and save the `IDKeeper`
        to the cache directory.

        Parameters
        ----------

        seasons : list[int]
            List of seasons to get draft data for
        """
        drafts_df = drafts.get(seasons, self.cache_path)
        for _, draft_series in tqdm.tqdm(
            iterable=drafts_df.iterrows(),
            desc="Updating the IDKeeper with drafted players data",
            total=len(drafts_df),
        ):
            ids = draft_series[
                [
                    drafts.cols.CfbPlayerId.header,
                    drafts.cols.PfrPlayerId.header,
                    "extra_ID",
                ]
            ].to_dict()
            self.append(ids)
        self.update_mapping()
        self.dump()

    def add_players(self, refresh_players: bool = False):
        """
        Add all players from `players.get()` to the `IDKeeper`, update the mapping, and save the `IDKeeper`
        to the cache directory. If `refreash_players` is `True`, `players.get()` will refresh the player data from the web source,
        otherwise it will use data stored in the cache if it exists.
        """
        players_df = players.get(self.cache_path, refresh_players)
        for _, player_series in tqdm.tqdm(
            iterable=players_df.iterrows(),
            desc="Updating the IDKeeper with players data",
            total=len(players_df),
        ):
            ids = player_series[
                [
                    players.cols.EsbId.header,
                    players.cols.GsisId.header,
                    players.cols.SmartId.header,
                    "extra_ID",
                ]
            ].to_dict()
            self.append(ids)
        self.update_mapping()
        self.dump()

    def add_rosters(self, seasons: list[int], update_last_season: bool = False):
        """
        Add all players from `rosters.get()` to the `IDKeeper`, update the mapping, and save the `IDKeeper`
        to the cache directory. If `update_last_season` is `True`, `rosters.get()` will refresh the last/current season's
        roster data from the web source, otherwise it will use data stored in the cache if it exists.
        """
        COLS = [
            rosters.cols.EsbId.header,
            rosters.cols.PffId.header,
            rosters.cols.PfrId.header,
            rosters.cols.EspnId.header,
            rosters.cols.SmartId.header,
            rosters.cols.YahooId.header,
            rosters.cols.PlayerId.header,
            rosters.cols.SleeperId.header,
            rosters.cols.RotowireId.header,
            rosters.cols.SportradarId.header,
            rosters.cols.FantasyDataId.header,
            "extra_ID",
        ]
        roster_df = rosters.get(seasons, self.cache_path, update_last_season)
        roster_df = roster_df[COLS].drop_duplicates()
        for _, roster_series in tqdm.tqdm(
            iterable=roster_df.iterrows(),
            desc="Updating the IDKeeper with rosters data",
            total=len(roster_df),
        ):
            ids = roster_series.to_dict()
            self.append(ids)
        self.update_mapping()
        self.dump()

    def refresh(self):
        season = current_season()
        years = [year for year in range(2002, season + 1)]
        print("Updating Draft Data:")
        self.add_drafts(years)
        print("Updating Player Data:")
        self.add_players(True)
        print("Updating Roster Data:")
        self.add_rosters(years, True)

    def __len__(self) -> int:
        return len(self.df)


class IDMap:
    def __init__(self):
        pass

    def load(self, cache_path: str):
        """
        Load the `IDMap` from the given cache directory or create one if it does not exist.

        Parameters
        ----------

        cache_path : str
            Cache directory location
        """
        self.cache_path = cache_path
        self.path = cache_path + cache.fname_players() + "-idmap.csv"
        self.df = pandas.DataFrame({id_header: [] for id_header in DTYPE_LIST})
        self.df = self.df.astype(dtype=DTYPE_LIST)
        if os.path.exists(self.path):
            self.df = pandas.concat(
                [self.df, pandas.read_csv(self.path, dtype=DTYPE_LIST)]
            )

    def dump(self):
        """
        Save the `IDMap` to the associated cach direcotry.
        """
        self.df.to_csv(self.path, index=False)

    def add_bi_map(self, update: bool = False):
        bi_map = get_mapping(self.cache_path, update)
        bi_map_cols = bi_map.columns.intersection(DTYPE_LIST).to_list()
        self.df = pandas.concat([self.df, bi_map[bi_map_cols]])

    def add_drafts(self, seasons: list[int]):
        draft_cols = [
            drafts.cols.CfbPlayerId.header,
            drafts.cols.PfrPlayerId.header,
            "extra_ID",
        ]
        drafts_df = drafts.get(seasons, self.cache_path)
        self.df = pandas.concat([self.df, drafts_df[draft_cols]])

    def add_players(self, update: bool = False):
        player_cols = [
            players.cols.EsbId.header,
            players.cols.GsisId.header,
            players.cols.SmartId.header,
            "extra_ID",
        ]
        players_df = players.get(self.cache_path, update)
        self.df = pandas.concat([self.df, players_df[player_cols]])

    def add_rosters(self, seasons: list[int], update: bool = False):
        roster_cols = [
            rosters.cols.EsbId.header,
            rosters.cols.PffId.header,
            rosters.cols.PfrId.header,
            rosters.cols.EspnId.header,
            rosters.cols.SmartId.header,
            rosters.cols.YahooId.header,
            rosters.cols.PlayerId.header,
            rosters.cols.SleeperId.header,
            rosters.cols.RotowireId.header,
            rosters.cols.SportradarId.header,
            rosters.cols.FantasyDataId.header,
            "extra_ID",
        ]
        roster_df = rosters.get(seasons, self.cache_path, update)
        self.df = pandas.concat([self.df, roster_df[roster_cols].drop_duplicates()])

    def _unify_get_match_indexes(self, column: str, index: int) -> list[int]:
        matches = self.df[self.df[column] == self.df[column].iloc[index]]
        matches = matches.dropna(axis=1)
        is_match = matches.eq(matches.loc[index]).all(axis=1)
        is_match = is_match & (is_match.index != index)
        indexes = is_match.index[is_match]
        return list(indexes)

    def _unify_column(self, column: str):
        dupes = self.df[column].duplicated() & self.df[column].notna()
        for index, is_dup in dupes.items():
            if is_dup:
                match_indexes = self._unify_get_match_indexes(column, index)
                if len(match_indexes) > 1:
                    for match_index in match_indexes:
                        new_series = self.df.iloc[index].combine_first(
                            self.df.iloc[match_index]
                        )
                        self.df.iloc[index] = new_series
                        self.df.iloc[match_index] = new_series

    def drop_duplicates(self):
        self.df = self.df.drop_duplicates()
        self.df = self.df.reset_index(drop=True)

    def maptize(self):
        self.drop_duplicates()
        self.df = self.df.replace(0, None)
        for column in tqdm.tqdm(self.df.columns, total=len(self.df.columns)):
            self._unify_column(column)
            self.drop_duplicates()
