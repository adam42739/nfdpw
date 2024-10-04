import pandas
import json
import os


def fname_pbp(season: int) -> str:
    return "pbp-" + str(season)


def fname_schedules(season: int) -> str:
    return "schedules-" + str(season)


def fname_rosters(season: int) -> str:
    return "rosters-" + str(season)


def fname_players() -> str:
    return "players"

def fname_superbowls() -> str:
    return "sbowls"


def load(cache_path: str, fname: str) -> pandas.DataFrame:
    path = cache_path + fname + ".parq"
    return pandas.read_parquet(path)


def dump(df: pandas.DataFrame, cache_path: str, fname: str):
    path = cache_path + fname + ".parq"
    df.to_parquet(path)


def load_mdata(cache_path: str, mdata_type: str) -> dict:
    mdata = {}
    path = cache_path + "_mdata-" + mdata_type + ".json"
    if os.path.exists(path):
        with open(path, "r") as file:
            mdata = json.load(file)
    return mdata


def dump_mdata(mdata: dict, cache_path: str, mdata_type: str):
    with open(cache_path + "_mdata-" + mdata_type + ".json", "w") as file:
        json.dump(mdata, file)


def load_pbp_mdata(cache_path: str) -> dict:
    mdata = load_mdata(cache_path, "pbp")
    new_mdata = {}
    for season in mdata:
        new_mdata[int(season)] = mdata[season]
    return new_mdata


def dump_pbp_mdata(mdata: dict, cache_path: str):
    dump_mdata(mdata, cache_path, "pbp")


def load_schedules_mdata(cache_path: str) -> dict:
    mdata = load_mdata(cache_path, "schedules")
    new_mdata = {}
    for season in mdata:
        new_mdata[int(season)] = True
    return new_mdata


def dump_schedules_mdata(mdata: dict, cache_path: str):
    dump_mdata(mdata, cache_path, "schedules")


def load_rosters_mdata(cache_path: str) -> dict:
    mdata = load_mdata(cache_path, "rosters")
    new_mdata = {}
    for season in mdata:
        new_mdata[int(season)] = True
    return new_mdata


def dump_rosters_mdata(mdata: dict, cache_path: str):
    dump_mdata(mdata, cache_path, "rosters")
