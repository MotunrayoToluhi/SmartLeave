import requests
from datetime import datetime
from Static_Data.DateCategories import seasons_data

# app.route() as an abstract method for oop?
# helen showed this at the beginning of lesson
def get_API_holidays():
    url = 'https://www.gov.uk/bank-holidays.json'
    response = requests.get(url)
    all_holidays = response.json()
    return all_holidays["england-and-wales"]["events"]


holidays = get_API_holidays()

# getting just bank holidays as dates
def just_bank_holidays(hols_list):
    first_list_of_dates = []
    list_of_dates = []
    for each in hols_list:
        first_list_of_dates.append(each['date'])
    for x in first_list_of_dates:
        date_x = datetime.strptime(x, '%Y-%m-%d').date()
        list_of_dates.append(date_x)
    return list_of_dates

bank_holidays = just_bank_holidays(holidays)

# categorizing the holidays gotten from the api into seasons
def categorize_by_season():

    holidays_by_season = {
        "winter_holidays": [],
        "spring_holidays": [],
        "summer_holidays": [],
        "autumn_holidays": []
    }

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
    return holidays_by_season


categorized_holiday = categorize_by_season()

#
# # Test dictionary
# print(categorized_holiday)
# for key, holidays_list in categorized_holiday.items():
#     print(f"{key}: {holidays_list}")
