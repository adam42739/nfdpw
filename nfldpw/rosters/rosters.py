import nfl_data_py
from .. import cache
import pandas
from .. import sbowls


def _season_complete(df: pandas.DataFrame) -> bool:
    for sb in sbowls.WEEKS:
        count = ((df["season"] == sb["season"]) & (df["week"] == sb["week"])).sum()
        if count > 0:
            return True
    return False


def get(seasons: list[int], cache_path: str = None) -> pandas.DataFrame:
    """
    Get roster data for the list of seasons provided.
    If a cache path is provided, data will be read from the cache
    or stored in the cache if calling for the first time. Otherwise,
    data is loaded from the web source.

    Parameters
    ----------

    seasons : list[int]
        Seasons to get roster data for

    cache_path : str = None
        Path to a directory where cache files are stored

    Returns
    -------

        out : pandas.DataFrame

    Examples
    --------

        >>> rosters.get([2020, 2021, 2022], "path_to_cache/")
    """
    dfs = []
    if cache_path:
        mdata = cache.load_rosters_mdata(cache_path)
        dfs = []
        for season in seasons:
            if season in mdata:
                dfs.append(cache.load(cache_path, cache.fname_rosters(season)))
            else:
                df = nfl_data_py.import_weekly_rosters([season])
                if _season_complete(df):
                    cache.dump(df, cache_path, cache.fname_rosters(season))
                    mdata[season] = True
                    cache.dump_rosters_mdata(mdata, cache_path)
                dfs.append(df)

    else:
        for season in seasons:
            dfs.append(nfl_data_py.import_seasonal_rosters([season]))
    return pandas.concat(dfs)
