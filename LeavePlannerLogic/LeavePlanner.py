from datetime import datetime
from Static_data.DateCategories import seasons_data
from LeavePlannerLogic.API_Logic.Holiday_api import categorized_holiday


# Asking the user how many days of leave that they have a year
def leave_entitlement():
    while True:
        max_leave = input(f"How many leave days are you entitled to per year?: ")
        if max_leave.isdigit():
            max_leave = int(max_leave)
            if 0 < max_leave < 365:
                break
            else:
                print("Days must be more than zero and less than 365.")
        else:
            print(f"Please enter valid positive a number.")
    return max_leave


max_leave = leave_entitlement()


# calculating the amount of leave that the user has left
# need to create a function to calculate leave taken after the function to calculate
# what dates the user should take off are done
def calc_leave_left():
    remaining_leave = max_leave - leave_taken
    return remaining_leave


# function to ask the user what season they want their next holiday to be in
def user_chosen_season():
    while True:
        preferred_season = input(f"What do you want to go on holiday in? (Winter, Spring, Summer, Autumn): ")
        preferred_season = preferred_season.lower()
        if preferred_season in ["winter", "spring", "summer", "autumn"]:
            break
        else:
            print("Season must be Summer, Winter, Spring or Autumn")
    return preferred_season


# function to ask the user what year they want their next holiday to be in
def user_chosen_year():
    while True:
        preferred_year = input(f"What do you year to go on holiday in? (2023, 2024, 2025): ")
        preferred_year = preferred_year.lower()
        if preferred_year in ["2023", "2024", "2025"]:
            break
        else:
            print("year must be 2023, 2024 or 2025")
    return preferred_year


# function that asks the user how many days notice they need to give their employer before they take time off
def days_notice():
    while True:
        user_days_notice = input(f"How many days notice do you need to give your employer?: ")
        if user_days_notice.isdigit():
            user_days_notice = int(user_days_notice)
            if 0 < user_days_notice < 365:
                break
            else:
                print("Days must be more than zero and less than 365.")
        else:
            print(f"Please enter a valid positive number.")
    return user_days_notice


# asking the user how long they want their holiday to be
def holiday_length():
    while True:
        user_hol_len = input(f"How many days do you want to be on holiday for?: ")
        if user_hol_len.isdigit():
            user_hol_len = int(user_hol_len)
            if 0 < user_hol_len < 365:
                break
            else:
                print("Days must be more than zero and less than 365.")
        else:
            print(f"Please enter a valid positive number.")
    return user_hol_len


holiday_year = user_chosen_year()
holiday_season = user_chosen_season()


# filtering the bank holidays from the api based on the season
# that the user wants to go on holiday in
def filtered_season():
    filtered_holidays_season = {}
    for season, holidays in categorized_holiday.items():
        if "_holidays" in season:
            filtered_holidays_season[season] = holidays
    return filtered_holidays_season


# Sorting the bank holidays from the api based on the
# season and year that the user wants to go on holiday in

def filter_by_year(filtered_season_result, year, season):
    filtered_holidays_year = {}

    for key, holidays_list in filtered_season_result.items():
        season_key = key.replace("_holidays", "")
        if season_key == holiday_season:
            # filtered_holidays_year[season_key] = holidays_list
            filter_by_year_season = [holiday for holiday in holidays_list if holiday["date"].startswith(year)]
            filtered_holidays_year[season_key] = filter_by_year_season
    return filtered_holidays_year


# running and testing that the bank holidays based on the
# user preferences have been filtered properly
filtered_season_result = filtered_season()
filtered_year_season = filter_by_year(filtered_season_result, holiday_year, holiday_season)

# print(filtered_year_season)
# print(filtered_season_result)
# print(holiday_year)
# print(holiday_season)

def cal_holiday_date():

# backup function that filters the bank holidays from
# the api only based on the year that the user wants to go on holiday in
# (will delete when the whole app is functioning correctly)

# def filter_by_year(holiday=None):
#     filtered_holidays_year = {}
#
#     for season, holiday_list in categorized_holiday.items():
#         filter_by_year_season = [holiday for holiday in holiday_list if holiday["date"].startswith(holiday_year)]
#         filtered_holidays_year[season] = filter_by_year_season
#
#     return filtered_holidays_year
# print(filter_by_year())
