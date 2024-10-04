import nfl_data_py
import pandas
from .. import cache
from .. import sbowls


def _season_complete(df: pandas.DataFrame, cache_path: str) -> bool:
    sb_dates = sbowls.load_superbowl_dates(cache_path)
    sb_cands = pandas.to_datetime(df["game_date"]).isin(sb_dates).sum()
    complete = sb_cands > 0
    return complete


def get(seasons: list[int], cache_path: str = None) -> pandas.DataFrame:
    """
    Get play-by-play data for the list of seasons provided.
    If a cache path is provided, data will be read from the cache
    or stored in the cache if calling for the first time. Otherwise,
    data is loaded from the web source.

    Parameters
    ----------

    seasons : list[int]
        Seasons to get play-by-play data for

    cache_path : str = None
        Path to a directory where cache files are stored

    Returns
    -------

        out : pandas.DataFrame

    Examples
    --------

        >>> pbp.get([2020, 2021, 2022], "path_to_cache/")
    """
    dfs = []
    if cache_path:
        mdata = cache.load_pbp_mdata(cache_path)
        dfs = []
        for season in seasons:
            if season in mdata:
                dfs.append(cache.load(cache_path, cache.fname_pbp(season)))
            else:
                df = nfl_data_py.import_pbp_data([season])
                if _season_complete(df, cache_path):
                    cache.dump(df, cache_path, cache.fname_pbp(season))
                    mdata[season] = True
                    cache.dump_pbp_mdata(mdata, cache_path)
                dfs.append(df)

    else:
        for season in seasons:
            dfs.append(nfl_data_py.import_pbp_data([season]))
    return pandas.concat(dfs)
