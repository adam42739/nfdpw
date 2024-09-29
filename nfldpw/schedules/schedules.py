import pandas
import nfl_data_py
from .. import cache
from .. import sbowls


def _season_complete(df: pandas.DataFrame) -> bool:
    sb_cands = pandas.to_datetime(df["gameday"]).isin(sbowls.DATES).sum()
    complete = sb_cands > 0
    return complete


def get(seasons: list[int], cache_path: str = None) -> pandas.DataFrame:
    """
    Get schedules data for the list of seasons provided.
    If a cache path is provided, data will be read from the cache
    or stored in the cache if calling for the first time. Otherwise,
    data is loaded from the web source.

    Parameters
    ----------

    seasons : list[int]
        Seasons to get schedules data for

    cache_path : str = None
        Path to a directory where cache files will be stored

    Returns
    -------

        out : pandas.DataFrame

    Examples
    --------

        >>> schedules.get([2020, 2021, 2022], "path_to_cache/")
    """
    dfs = []
    if cache_path:
        mdata = cache.load_schedules_mdata(cache_path)
        dfs = []
        for season in seasons:
            if season in mdata:
                dfs.append(cache.load(cache_path, cache.fname_schedules(season)))
            else:
                df = nfl_data_py.import_schedules([season])
                if _season_complete(df):
                    cache.dump(df, cache_path, cache.fname_schedules(season))
                    mdata[season] = True
                    cache.dump_schedules_mdata(mdata, cache_path)
                dfs.append(df)

    else:
        for season in seasons:
            dfs.append(nfl_data_py.import_schedules([season]))
    return pandas.concat(dfs)
