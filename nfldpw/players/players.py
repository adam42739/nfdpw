import nfl_data_py
from .. import cache
import pandas
import os


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
    if cache_path:
        if (
            os.path.exists(cache_path + cache.fname_players() + ".parq")
            and refresh_cache == False
        ):
            return cache.load(cache_path, cache.fname_players())
        else:
            df = nfl_data_py.import_players()
            cache.dump(df, cache_path, cache.fname_players())
            return df
    else:
        return nfl_data_py.import_players()
