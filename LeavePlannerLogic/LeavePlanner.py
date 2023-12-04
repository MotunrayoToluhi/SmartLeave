from datetime import datetime
from Static_data.DateCategories import seasons_data


# def user_preferences():
#     while True:
#         remaining_leave = input(f"How many leave days do you have left to use? YYYY-MM-DD: ")
#         try:
#             date_obj = datetime.datetime.strptime(remaining_leave, "%Y-%m-%d")
#             break
#         except ValueError:
#             print(f"Incorrect date format, should be YYYY-MM-DD")
#
# user_preferences()

def initial_leave_left():
    while True:
        remaining_leave = input(f"How many leave days do you have left to use?: ")
        if remaining_leave.isdigit():
            remaining_leave = int(remaining_leave)
            if 0 < remaining_leave < 365:
                break
            else:
                print("Days must be more than zero and less than 365.")
        else:
            print(f"Please enter valid positive a number.")
    return remaining_leave


def user_chosen_season():
    while True:
        preferred_season = input(f"What do you want to go on holiday in? (Winter, Spring, Summer, Autumn): ")
        preferred_season = preferred_season.lower()
        if preferred_season in ["winter", "spring", "summer", "autumn"]:
            break
        else:
            print("Season must be Summer, Winter, Spring or Autumn")
    return preferred_season

def user_chosen_year():
    while True:
        preferred_year = input(f"What do you year to go on holiday in? (2023, 2024, 2025): ")
        preferred_year = preferred_year.lower()
        if preferred_year in ["2023", "2024", "2025"]:
            break
        else:
            print("year must be 2023, 2024 or 2025")
    return preferred_year


def days_notice():
    while True:
        user_days_notice = input(f"How many days days notice do you need to give your employer?: ")
        if user_days_notice.isdigit():
            user_days_notice = int(user_days_notice)
            if 0 < user_days_notice < 365:
                break
            else:
                print("Days must be more than zero and less than 365.")
        else:
            print(f"Please enter a valid positive number.")
    return user_days_notice

# def holidays_by_seasons():


# def holiday_range_calculator():
#     if user_chosen_season() in seasons_data:
#         month_names = seasons_data[season.lower()]
#         month_dates = [datetime.strptime(month, "%B").month for month in month_names]
#         return month_dates
#     else:
#         return None


# if user_chosen_season() in seasons_data:
#     print(f"yes")


# initial_leave_left()
# days_notice()
# user_chosen_season()
user_chosen_year()