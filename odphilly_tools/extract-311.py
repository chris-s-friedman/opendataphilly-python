import pandas as pd
import requests as re
from datetime import date
from dateutil import relativedelta
from tqdm import tqdm


def date_list_builder(start, stop):
    start_date = date.fromisoformat(start)
    stop_date = date.fromisoformat(stop)
    date_list = []
    while (stop_date - start_date).days > 0:
        diff = relativedelta.relativedelta(stop_date, start_date)
        diff_months = diff.months + diff.years * 12
        if diff_months > 0:
            date_list.append(
                {
                    "start": start_date,
                    "end": start_date + relativedelta.relativedelta(day=31),
                }
            )
            start_date = start_date + relativedelta.relativedelta(
                months=1, day=1
            )
        else:
            date_list.append({"start": start_date, "end": stop_date})
            start_date = stop_date
    return date_list


def query_constructor(start_date, end_date=None):
    columns = [
        "service_request_id",
        "status",
        "status_notes",
        "service_name",
        "service_code",
        "agency_responsible",
        "service_notice",
        "requested_datetime",
        "updated_datetime",
        "expected_datetime",
        "address",
        "zipcode",
        "media_url",
        "lat",
        "lon",
    ]
    column_str = str(columns)[1:-1].replace("'", "")
    base_query = f"SELECT {column_str} FROM public_cases_fc"
    where_clause = f"WHERE requested_datetime >= '{start_date}'"
    if end_date:
        where_clause = where_clause + f" AND requested_datetime < '{end_date}'"
    return base_query + " " + where_clause


def main(start, stop, cartodb_url="https://phl.carto.com/api/v2/sql"):
    date_list = date_list_builder(start, stop)
    responses = []
    for dates in tqdm(date_list):
        query = query_constructor(dates["start"], dates["end"])
        query_url = f"{cartodb_url}?q={query}"
        resp = re.get(query_url)
        responses.append(pd.DataFrame(resp.json()["rows"]))
    return pd.concat(responses)
