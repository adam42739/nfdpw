import nfl_data_py
from .. import cache
import pandas
from .. import sbowls
from . import cols
from ..drafts import EXTRA_DRAFT_ID
import datetime


DAYS_GREATER = 14


def _season_complete(season: int, cache_path: str) -> bool:
    sb_dates = sbowls.load_superbowl_dates(cache_path)
    for date in sb_dates:
        if date.year - 1 == season:
            if datetime.datetime.today() > date + datetime.timedelta(DAYS_GREATER):
                return True
    return False


NONE_CHAR = "$NONE$"


def _check_none(x: str) -> str | None:
    if NONE_CHAR in x:
        return None
    else:
        return x


def _drft_num(x: str | int) -> str:
    if isinstance(x, str):
        return str(round(float(x)))
    else:
        if x == 0:
            return NONE_CHAR
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
        df[cols.DraftClub.header].fillna(NONE_CHAR)
        + df[cols.DraftNumber.header].fillna(0).apply(_drft_num)
        + df[cols.FirstName.header]
        .str.replace(" ", "-", regex=False)
        .str.replace(".", "_", regex=False)
        + "-"
        + df[cols.LastName.header]
        .str.replace(" ", "-", regex=False)
        .str.replace(".", "_", regex=False)
    ).apply(_check_none)
    return df


def _roster_cols_rename(df: pandas.DataFrame) -> pandas.DataFrame:
    """
    Rename roster columns for consistency.

    Requiring Rename
    ----------------

    `"player_id" -> "gsis_id"`
    """
    RENAME_MAP = {
        "player_id": "gsis_id",
    }
    df = df.rename(RENAME_MAP, axis="columns")
    return df


def get(
    seasons: list[int], cache_path: str = None, update_last_season: bool = False
) -> pandas.DataFrame:
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

    update_last_season : bool = False
        Whether cached seasons that are incomplete should be reloaded (i.e. after a new week has ended).

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
            from_cache = True
            if season in mdata:
                if not mdata[season] and update_last_season:
                    from_cache = False
            else:
                from_cache = False
            if from_cache:
                dfs.append(cache.load(cache_path, cache.fname_rosters(season)))
            else:
                df = nfl_data_py.import_weekly_rosters([season])
                if _season_complete(season, cache_path):
                    mdata[season] = True
                else:
                    mdata[season] = False
                cache.dump(df, cache_path, cache.fname_rosters(season))
                cache.dump_rosters_mdata(mdata, cache_path)
                dfs.append(df)
    else:
        for season in seasons:
            dfs.append(nfl_data_py.import_weekly_rosters([season]))
    df = pandas.concat(dfs)
    df = _roster_cols_rename(df)
    df = _create_extra_ID(df)
    return df
