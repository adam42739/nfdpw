import nfl_data_py
import pandas
from .. import cache


def get(seasons: list[int], cache_path: str = None) -> pandas.DataFrame:
    """
    Get draft data for the list of seasons provided.
    If a cache path is provided, data will be read from the cache
    or stored in the cache if calling for the first time. Otherwise,
    data is loaded from the web source.

    Parameters
    ----------

    seasons : list[int]
        Seasons to get play-by-play data for.

    cache_path : str = None
        Path to a directory where cache files are stored.

    Returns
    -------

        out : pandas.DataFrame

    Examples
    --------

        >>> drafts.get([2020, 2021, 2022], "path_to_cache/")
    """
    dfs = []
    if cache_path:
        mdata = cache.load_drafts_mdata(cache_path)
        dfs = []
        for season in seasons:
            from_cache = True
            if season not in mdata:
                from_cache = False
            if from_cache:
                dfs.append(cache.load(cache_path, cache.fname_drafts(season)))
            else:
                df = nfl_data_py.import_draft_picks([season])
                if len(df) > 0:
                    mdata[season] = True
                    cache.dump(df, cache_path, cache.fname_drafts(season))
                    cache.dump_drafts_mdata(mdata, cache_path)
                    dfs.append(df)

    else:
        for season in seasons:
            dfs.append(nfl_data_py.import_draft_picks([season]))
    return pandas.concat(dfs)
