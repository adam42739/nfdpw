import nfl_data_py
from . import cols
import pandas
from .. import cache


EXTRA_DRAFT_ID = "extra_ID"


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
    picklesseq32 = df[cols.Pick.header] <= 32
    pick_num = (picklesseq32 * df[cols.Round.header] * df[cols.Pick.header]) + (
        (~picklesseq32) * df[cols.Pick.header]
    )
    df[EXTRA_DRAFT_ID] = (
        df[cols.Team.header]
        + (pick_num).apply(str)
        + df[cols.PfrPlayerName.header]
        .str.replace(" ", "-", regex=False)
        .str.replace(".", "_", regex=False)
    )
    return df


def _draft_cols_rename(df: pandas.DataFrame) -> pandas.DataFrame:
    """
    Rename draft columns for consistency.

    Requiring Rename
    ----------------

    `"cfb_player_id" -> "cfbref_id"`

    `"pfr_player_id" -> "pfr_id"`
    """
    RENAME_MAP = {
        "cfb_player_id": "cfbref_id",
        "pfr_player_id": "pfr_id",
    }
    df = df.rename(RENAME_MAP, axis="columns")
    return df


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
    df = pandas.concat(dfs)
    df = _draft_cols_rename(df)
    df = _create_extra_ID(df)
    return df
