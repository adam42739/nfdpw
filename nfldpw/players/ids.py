import pandas
import os
import nfl_data_py
from .. import cache
from .. import players
from ..drafts import EXTRA_DRAFT_ID

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

LIST = [
    YAHOO,
    ESB,
    SMART,
    NFL,
    ESPN,
    ROTOWORLD,
    GSIS,
    SLEEPER,
    STATS,
    SPORTRADAR,
    CBS,
    STATS_GLOBAL,
    CFBREF,
    FLEAFLICKER,
    FANTASYPROS,
    FANTASY_DATA,
    PFF,
    MFL,
    PFR,
    ROTOWIRE,
    KTC,
    SWISH,
    EXTRA_DRAFT_ID,
]


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
    def __init__(self):
        pass

    def _path(self, cache_path: str) -> str:
        return cache_path + cache.fname_players() + "-idkeeper.csv"

    def load(self, cache_path: str):
        self.cache_path = cache_path
        path = self._path(cache_path)
        self.df = pandas.DataFrame({id_header: [] for id_header in LIST})
        if os.path.exists(path):
            self.df = pandas.concat([self.df, pandas.read_csv(path, index_col=0)])

    def dump(self):
        path = self._path(self.cache_path)
        self.df.to_csv(path, index=True)

    def exists(self, id_dict: dict[str, str]):
        for id in id_dict:
            if id_dict[id] in self.df[id].values:
                return True
        return False

    def append(self, id_dict: dict[str, str]):
        if not self.exists(id_dict):
            row = {id: None for id in LIST}
            for id in id_dict:
                row[id] = id_dict[id]
            self.df.loc[len(self)] = row

    def _update_mapping(self, id_map: pandas.DataFrame):
        for index in self.df.index:
            id_dict = self.df.iloc[index].dropna().to_dict()
            series = locate_map(id_map, id_dict)
            if not series.empty:
                series_dict = series.to_dict()
                for id in series_dict:
                    self.df.at[index, id] = series_dict[id]

    def update_mapping(self, update_map=False):
        id_map = get_mapping(self.cache_path, update_map)
        id_list = []
        for id in LIST:
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
        self._update_mapping(id_map)
        self._update_mapping(player_map)
        self._update_mapping(id_map)

    def __len__(self):
        return len(self.df)
