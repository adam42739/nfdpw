import pandas
import os
from . import drafts
import types
import nfl_data_py


MODULE_DEFAULT = "mdef"

YAHOO = {MODULE_DEFAULT: "yahoo_id"}
ESB = {MODULE_DEFAULT: "esb_id"}
SMART = {MODULE_DEFAULT: "smart_id"}
NFL = {MODULE_DEFAULT: "nfl_id"}
ESPN = {MODULE_DEFAULT: "espn_id"}
ROTOWORLD = {MODULE_DEFAULT: "rotoworld_id"}
GSIS = {MODULE_DEFAULT: "gsis_id"}
SLEEPER = {MODULE_DEFAULT: "sleeper_id"}
STATS = {MODULE_DEFAULT: "stats_id"}
SPORTRADAR = {MODULE_DEFAULT: "sportradar_id"}
CBS = {MODULE_DEFAULT: "cbs_id"}
STATS_GLOBAL = {MODULE_DEFAULT: "stats_global_id"}
CFBREF = {MODULE_DEFAULT: "cfbref_id", drafts: "cfb_player_id"}
FLEAFLICKER = {MODULE_DEFAULT: "fleaflicker_id"}
FANTASYPROS = {MODULE_DEFAULT: "fantasypros_id"}
FANTASY_DATA = {MODULE_DEFAULT: "fantasy_data_id"}
PFF = {MODULE_DEFAULT: "pff_id"}
MFL = {MODULE_DEFAULT: "mfl_id"}
PFR = {MODULE_DEFAULT: "pfr_id", drafts: "pfr_player_id"}
ROTOWIRE = {MODULE_DEFAULT: "rotowire_id"}
KTC = {MODULE_DEFAULT: "ktc_id"}
SWISH = {MODULE_DEFAULT: "swish_id"}


def id_col(id: dict[str | types.ModuleType, str], module: types.ModuleType) -> str:
    if module in id:
        return id[module]
    else:
        return id[MODULE_DEFAULT]


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
        path = cache_path + "player_ids.csv"
        if os.path.exists(path) and refresh == False:
            return pandas.read_csv(path)
        else:
            df = nfl_data_py.import_ids()
            df.to_csv(path)
            return df
    else:
        return nfl_data_py.import_ids()


def id_map_lookup(
    id_map: pandas.DataFrame, ids: dict[int, str]
) -> pandas.Series | None:
    for id_key_index in ids:
        id_key = LIST[id_key_index]
        id = ids[id_key_index]
        if id_key[MODULE_DEFAULT] in id_map.columns:
            mask = id_map[id_key[MODULE_DEFAULT]] == id
            df = id_map[mask]
            if not df.empty:
                return df.iloc[0]
    return None
