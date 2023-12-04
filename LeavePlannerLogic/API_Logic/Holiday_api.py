import requests
from datetime import datetime, timedelta
from Static_data.DateCategories import seasons_data


# app.route()
def get_API_holidays():
    url = 'https://www.gov.uk/bank-holidays.json'
    response = requests.get(url)
    all_holidays = response.json()
    return all_holidays["england-and-wales"]["events"]


holidays = get_API_holidays()

holidays_by_season = {
    "winter_holidays": [],
    "spring_holidays": [],
    "summer_holidays": [],
    "autumn_holidays": []
}


def categorize_by_season():
    for event in holidays:
        event_date_str = event["date"]
        event_title = event["title"]

        event_date = datetime.strptime(event_date_str, "%Y-%m-%d")

        for season, months in seasons_data.items():
            for month, _ in months:
                if event_date.month == month:
                    holidays_by_season[season + "_holidays"].append({
                        "title": event_title,
                        "date": event_date_str
                    })
                    break


categorize_by_season()

for key, holidays_list in holidays_by_season.items():
    print(f"{key}: {holidays_list}")
