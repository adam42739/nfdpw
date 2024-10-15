import nfl_data_py
from .. import cache
from . import cols
import pandas
import os
import numpy
from ..drafts import EXTRA_DRAFT_ID


def _rounder(x: numpy.float32) -> str:
    if numpy.isnan(x):
        return ""
    else:
        return str(round(x))


def _create_extra_ID(df: pandas.DataFrame) -> pandas.DataFrame:
    df[EXTRA_DRAFT_ID] = (
        df[cols.DraftClub.header]
        + df[cols.DraftNumber.header].apply(_rounder)
        + df[cols.FirstName.header]
        .str.replace(" ", "-", regex=False)
        .str.replace(".", "_", regex=False)
        + "-"
        + df[cols.LastName.header]
        .str.replace(" ", "-", regex=False)
        .str.replace(".", "_", regex=False)
    )
    return df


def get(cache_path: str = None, refresh_cache: bool = False) -> pandas.DataFrame:
    """
    Get descriptive player data. If a cache path is provided, data will be read
    from the cache or stored in the cache if calling for the first time. Otherwise,
    data is loaded from the web source. Pass `refresh_cache = True` to refresh the cache
    in case of new players entering the league (i.e. after the draft).

    Parameters
    ----------

    cache_path : str = None
        Path to a directory where cache files are stored

    refresh_cache : bool = False
        Whether or not the cache should be refreshed with the most up-to-date player data.

    Returns
    -------

        out : pandas.DataFrame

    Examples
    --------

        >>> players.get("path_to_cache/")
    """
    df = pandas.DataFrame()
    if cache_path:
        if (
            os.path.exists(cache_path + cache.fname_players() + ".parq")
            and refresh_cache == False
        ):
            df = cache.load(cache_path, cache.fname_players())
        else:
            df = nfl_data_py.import_players()
            cache.dump(df, cache_path, cache.fname_players())
    else:
        df = nfl_data_py.import_players()
    df = _create_extra_ID(df)
    return df
