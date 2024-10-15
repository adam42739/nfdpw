import nfl_data_py
from . import cols
import pandas
from .. import cache


EXTRA_DRAFT_ID = "extra_ID"


def _create_extra_ID(df: pandas.DataFrame) -> pandas.DataFrame:
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
