import pandas
import os
import nfl_data_py
from .. import cache
from .. import players
from .. import drafts
from ..drafts import EXTRA_DRAFT_ID
import tqdm

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
        self.df = pandas.DataFrame({id_header: [] for id_header in LIST})
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
            row = {id: None for id in LIST}
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
        for index, draft_series in tqdm.tqdm(
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

    def __len__(self) -> int:
        return len(self.df)
