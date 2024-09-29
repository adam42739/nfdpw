import pandas
import json
import os


def fname_pbp(season: int) -> str:
    return "pbp-" + str(season)


def load(cache_path: str, fname: str) -> pandas.DataFrame:
    path = cache_path + fname + ".parq"
    return pandas.read_parquet(path)


def dump(df: pandas.DataFrame, cache_path: str, fname: str):
    path = cache_path + fname + ".parq"
    df.to_parquet(path)


def load_mdata(cache_path: str) -> dict:
    mdata = {}
    path = cache_path + "_mdata.json"
    if os.path.exists(path):
        with open(path, "r") as file:
            mdata = json.load(file)
    return mdata


def dump_mdata(mdata: dict, cache_path: str):
    with open(cache_path + "_mdata.json", "w") as file:
        json.dump(mdata, file)


def load_pbp_mdata(cache_path: str) -> dict:
    mdata = load_mdata(cache_path)
    new_mdata = {}
    for season in mdata:
        new_mdata[int(season)] = True
    return new_mdata


def dump_pbp_mdata(mdata: dict, cache_path: str):
    dump_mdata(mdata, cache_path)
