import datetime
import pandas
import requests
import io
import json
from .cache import cache
import os


SBOWL_LINK = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
PAST_BOWLS_TABLE_INDEX = 1
FUTURE_BOWLS_TABLE_INDEX = 2


def _parse_raw_date(date_raw: str) -> datetime.datetime:
    count = 0
    index = 0
    while index < len(date_raw):
        if date_raw[index] == " ":
            count += 1
            if count == 3:
                break
        index += 1
    date_str = date_raw[:index]
    return datetime.datetime.strptime(date_str, "%B %d, %Y")


def _get_table_dates(df: pandas.DataFrame) -> list[datetime.datetime]:
    dates_raw = df["Date/Season"]
    dates = []
    for date_raw in dates_raw:
        dates.append(_parse_raw_date(date_raw))
    return dates


def _get_sbowls() -> list[datetime.datetime]:
    text = requests.get(SBOWL_LINK).text
    tables = pandas.read_html(io.StringIO(text))
    past = tables[PAST_BOWLS_TABLE_INDEX]
    future = tables[FUTURE_BOWLS_TABLE_INDEX]
    past_dates = _get_table_dates(past)
    future_dates = _get_table_dates(future)
    return past_dates + future_dates


def load_superbowl_dates(
    cache_path: str = None, update_cache: bool = False
) -> list[datetime.datetime]:
    """
    Load all past and scheduled future Super Bowl dates using Wikopedia.
    If `cache_path` is given, load from the cache unless `update_cache = True` in which case data
    is loaded from Wikopedia and used to update the cache.
    """
    if cache_path:
        if update_cache:
            dates = _get_sbowls()
            dates_str = []
            for i in range(0, len(dates)):
                dates_str.append(datetime.datetime.strftime(dates[i], "%Y%m%d"))
            with open(cache_path + cache.fname_superbowls() + ".json", "w") as file:
                json.dump(dates_str, file)
            return dates
        else:
            dates = []
            path = cache_path + cache.fname_superbowls() + ".json"
            if os.path.exists(path):
                with open(path, "r") as file:
                    dates = json.load(file)
                for i in range(0, len(dates)):
                    dates[i] = datetime.datetime.strptime(dates[i], "%Y%m%d")
            return dates
    else:
        return _get_sbowls()
