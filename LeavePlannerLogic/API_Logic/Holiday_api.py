import requests
from datetime import datetime, timedelta
from Static_data.DateCategories import seasons_data


def get_API_holidays():
    url = 'https://www.gov.uk/bank-holidays.json'
    response = requests.get(url)
    all_holidays = response.json()
    return all_holidays["england-and-wales"]["events"]


holidays = get_API_holidays()

winter_holidays = {}
spring_holidays = {}
summer_holidays = {}
autumn_holidays = {}


def categorize_by_season():
    for event in holidays:
        event_date_str = event["date"]
        event_title = event["title"]

        event_date = datetime.strptime(event_date_str, "%Y-%m-%d")

        for season, months in seasons_data.items():
            for month, _ in months:
                if event_date.month == month:
                    seasons_data[season].append({
                        "title": event_title,
                        "date": event_date_str
                    })
                    break

categorize_by_season()

print()

# for season_name, events in seasons_data.items():
#     seasons_data[season_name] = sorted(events, key=lambda x: x["date"])


# def categorize_by_season(event_title, event_date, seasons_data):
# def categorize_by_season():
#     for event in holidays:
#         event_date = event["date"]
#         event_title = event["title"]
#     date_format = datetime.strptime(event_date, "%Y-%M-%D")
#     for season, months in seasons_data.items()
#         for month, i in months:
#             if date_format == month:
#                 season_data[season]


# Test to see if righ info is given
# print(event_title)
# print(event_date)
# print("---------")

#     event_date = datetime.strptime(event_date, "%Y-%m-%d")
#     for season, months in seasons_data.items():
#         for month, i in months:
#             if event_date.month == month:
#                 seasons_data[season].append(event_date.strftime("%Y-%m-%d"))


# print("Title:", event["title"])
# print("Date:", event["date"])

