#!/usr/bin/env python3

import json
from typing import Dict

import requests

url = "https://farsicalendar.com/api/"
sale_shamsi_ghamari = {
    "sh": {
        1: 31,
        2: 31,
        3: 31,
        4: 31,
        5: 31,
        6: 31,
        7: 30,
        8: 30,
        9: 30,
        10: 30,
        11: 30,
        12: 30,
    },
    "ic": {
        1: 30,
        2: 30,
        3: 30,
        4: 30,
        5: 30,
        6: 30,
        7: 30,
        8: 30,
        9: 30,
        10: 30,
        11: 30,
        12: 30,
    },
}


def get(day: int, month: int, year_type: str) -> Dict:
    """A function for receiving calendar occasions from the x.y site

    Args:
        day (int): day number of the month
        month (int): month number of the year
        year_type (str): Type of calendars supported in the api
    Returns:
        Dict: Return Json Posted by api
    """
    return json.loads(requests.get(f"{url}{year}/{day}/{month}").content)


for year in sale_shamsi_ghamari:
    year_occasions = {}
    for month, days in sale_shamsi_ghamari[year].items():
        month_occasions = {}
        for day in range(1, days + 1):
            day_occasions = get(day, month, year_type=year)["values"]
            if day_occasions:
                month_occasions[day] = day_occasions[0]["occasion"]
            else:
                month_occasions[day] = None
            print(year, month, day, month_occasions[day])

        year_occasions[month] = month_occasions

    with open(f"year_occasions.{year}.json", "w", encoding="utf8") as f:
        json.dump(year_occasions, f, ensure_ascii=False)
