import nfl_data_py
from .. import cache
from . import cols
import pandas
import os
import numpy
from ..drafts import EXTRA_DRAFT_ID


def _rounder(x: numpy.float32) -> str:
    """
    Simple rounder applied to a data series in `_create_extra_ID()`. Converts `WXY.Z` to `"WXY"`. Returns `""` for `NaN`.
    """
    if numpy.isnan(x):
        return ""
    else:
        return str(round(x))


def _create_extra_ID(df: pandas.DataFrame) -> pandas.DataFrame:
    """
    Create the extra draft ID.

    -----
    Style
    -----

    id = [Draft Team][Draft Number Ovr (i.e. `round * pick`)][Full Name]

    Notes
    -----

    * In [Full Name], "." is replaced by "_" and " " is replaced by "-".

    * Depending on when a player was drafted, their Draft ID may show up with outdated team abbreviations (e.i. "STL", "SD", etc.).
    However, this should **_not_** be cause for concern as most sources where Draft IDs are generated from are consistent with the outdated
    team abbreviations.

    -------
    Example
    -------

    E.J. Henderson: Drafted 40th overall by the Minnesoda Vikings

    `MIN40E_J_-Henderson`

    ------------
    Known Issues
    ------------

    * Some sources might stylize E.J. Henderson's name as "Eric Henderson".
    In this case the auto-generated draft ID would be created as `MIN40Eric-Henderson` and will not
    match when compared against `MIN40E_J_-Henderson`.

    * Additionally, as it might be apparent, Draft ID is not 100% unique, but rather an auto-generated ID used to assist
    in matching players between different data sources. Inappropriate matches may occur, although they should be very rare.

    """
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
