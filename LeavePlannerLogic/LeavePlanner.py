import datetime
from LeavePlannerLogic.Holiday_api import categorized_holiday, bank_holidays


# FUNCTIONALITY THAT IS NOT IN OOP
# WILL DELETE WHEN EVERYTHING WORKS
class LeavePlannerFunc:
    def __init__(self):
        self.next_bank = self.next_bank_holiday()
        self.birthday = self.birthday_off()
        self.max_leave = self.leave_entitlement()
        self.leave_taken = 0
        self.days_of_holiday = self.holiday_length()
        self.holiday_year = self.user_chosen_year()
        self.holiday_season = self.user_chosen_season()
        self.filtered_season_result = self.filtered_season()
        self.filtered_year_season = self.filter_by_year(
            self.filtered_season_result, self.holiday_year, self.holiday_season
        )
        self.date_list = [holiday["date"] for holiday in self.filtered_year_season[self.holiday_season]]
        self.date_obj_list = [datetime.datetime.strptime(date_str, "%Y-%m-%d") for date_str in self.date_list]


    # function to get next bank holiday
    def next_bank_holiday(bank_hol):
        today = datetime.datetime.now().date()
        next_one = min(bank_holidays, key=lambda x: abs(x - today))
        return next_one

    # function check if birthday lands on weekend or AL or neither
    def birthday_off(birthday):
        date_birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d').date()
        print(date_birthday)
        bday_hol = any(date_birthday == num for num in bank_holidays)
        print(bday_hol)
        if bday_hol == False:
            if date_birthday.weekday() >= 5:
                return True
            elif date_birthday.weekday() < 5:
                return False
        else:
            return True

    # need to re-write this in to __init__
    def maximise(listofbankhols, year):
        # getting just that years holidays plus new years day
        next_year = int(year) + 1
        the_year = datetime.datetime.strptime(year, '%Y').date()
        next_year = datetime.datetime.strptime(str(next_year), '%Y').date()
        this_years_bank_hols = [date for date in listofbankhols if the_year <= date <= next_year]
        time_differences = []
        # getting the lenght of time between bank holidays
        l = len(this_years_bank_hols)
        seven_days = datetime.timedelta(days=7)
        for i in range(l):
            for x in range(i + 1, l):
                days = this_years_bank_hols[x] - this_years_bank_hols[i]
                # get all bank holidays that have less than a week between them
                if days <= seven_days:
                    return (days, this_years_bank_hols[x], this_years_bank_hols[i])
                # print(this_years_bank_hols[x], this_years_bank_hols[i], days)

    # print(maximise(bank_holidays, '2024'))

    def leave_entitlement(self):
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

    def calc_leave_left(self):
        remaining_leave = self.max_leave - self.leave_taken
        return remaining_leave

    def user_chosen_season(self):
        while True:
            preferred_season = input(f"What do you want to go on holiday in? (Winter, Spring, Summer, Autumn): ")
            preferred_season = preferred_season.lower()
            if preferred_season in ["winter", "spring", "summer", "autumn"]:
                break
            else:
                print("Season must be Summer, Winter, Spring, or Autumn")
        return preferred_season

    def user_chosen_year(self):
        while True:
            preferred_year = input(f"What do you year to go on holiday in? (2023, 2024, 2025): ")
            preferred_year = preferred_year.lower()
            if preferred_year in ["2023", "2024", "2025"]:
                break
            else:
                print("year must be 2023, 2024 or 2025")
        return preferred_year

    def days_notice(self):
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

    def holiday_length(self):
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

    def filtered_season(self):
        filtered_holidays_season = {}
        for season, holidays in categorized_holiday.items():
            if "_holidays" in season:
                filtered_holidays_season[season] = holidays
        return filtered_holidays_season

    def filter_by_year(self, filtered_season_result, year, season):
        filtered_holidays_year = {}
        for key, holidays_list in filtered_season_result.items():
            season_key = key.replace("_holidays", "")
            if season_key == season:
                filter_by_year_season = [holiday for holiday in holidays_list if holiday["date"].startswith(year)]
                filtered_holidays_year[season_key] = filter_by_year_season
        return filtered_holidays_year

    def calc_holiday_date(self):
        holiday_results = []

        for date_obj in self.date_obj_list:
            hol_start = date_obj.date() - timedelta(days=2)
            hol_end = hol_start + timedelta(days=self.days_of_holiday)
            final_holiday = print("You will be on holiday from", hol_start, "till", hol_end)
            if date_obj.weekday() == 0 or date_obj.weekday() == 4:  # 0 is Monday, 4 is Friday
                return final_holiday
            else:
                holiday_results.append(final_holiday)

        if not any(holiday_results):
            hol_start = datetime(year=int(self.holiday_year), month=9, day=1)
            while hol_start.weekday() != 5:  # 5 is Saturday
                hol_start += timedelta(days=1)
            hol_end = hol_start + timedelta(days=self.days_of_holiday)
            final_holiday = print("You will be on holiday from", hol_start.date(), "till", hol_end.date())
            return final_holiday


if __name__ == "__main__":
    leave_planner = LeavePlanner()
    leave_planner.calc_holiday_date()


# FUNCTIONALITY THAT IS NOT IN OOP
# WILL DELETE WHEN EVERYTHING WORKS
# # Asking the user how many days of leave that they have a year
# def leave_entitlement():
#     while True:
#         max_leave = input(f"How many leave days are you entitled to per year?: ")
#         if max_leave.isdigit():
#             max_leave = int(max_leave)
#             if 0 < max_leave < 365:
#                 break
#             else:
#                 print("Days must be more than zero and less than 365.")
#         else:
#             print(f"Please enter valid positive a number.")
#     return max_leave
#
#
# max_leave = leave_entitlement()
#
#
# # calculating the amount of leave that the user has left
# # need to create a function to calculate leave taken after the function to calculate
# # what dates the user should take off are done
# def calc_leave_left():
#     remaining_leave = max_leave - leave_taken
#     return remaining_leave
#
#
# # function to ask the user what season they want their next holiday to be in
# def user_chosen_season():
#     while True:
#         preferred_season = input(f"What do you want to go on holiday in? (Winter, Spring, Summer, Autumn): ")
#         preferred_season = preferred_season.lower()
#         if preferred_season in ["winter", "spring", "summer", "autumn"]:
#             break
#         else:
#             print("Season must be Summer, Winter, Spring or Autumn")
#     return preferred_season
#
#
# # function to ask the user what year they want their next holiday to be in
# def user_chosen_year():
#     while True:
#         preferred_year = input(f"What do you year to go on holiday in? (2023, 2024, 2025): ")
#         preferred_year = preferred_year.lower()
#         if preferred_year in ["2023", "2024", "2025"]:
#             break
#         else:
#             print("year must be 2023, 2024 or 2025")
#     return preferred_year
#
#
# # function that asks the user how many days notice they need to give their employer before they take time off
# def days_notice():
#     while True:
#         user_days_notice = input(f"How many days notice do you need to give your employer?: ")
#         if user_days_notice.isdigit():
#             user_days_notice = int(user_days_notice)
#             if 0 < user_days_notice < 365:
#                 break
#             else:
#                 print("Days must be more than zero and less than 365.")
#         else:
#             print(f"Please enter a valid positive number.")
#     return user_days_notice
#
#
# # asking the user how long they want their holiday to be
# def holiday_length():
#     while True:
#         user_hol_len = input(f"How many days do you want to be on holiday for?: ")
#         if user_hol_len.isdigit():
#             user_hol_len = int(user_hol_len)
#             if 0 < user_hol_len < 365:
#                 break
#             else:
#                 print("Days must be more than zero and less than 365.")
#         else:
#             print(f"Please enter a valid positive number.")
#     return user_hol_len
#
# days_of_holiday = holiday_length()
# holiday_year = user_chosen_year()
# holiday_season = user_chosen_season()
#
#
# # filtering the bank holidays from the api based on the season
# # that the user wants to go on holiday in
# def filtered_season():
#     filtered_holidays_season = {}
#     for season, holidays in categorized_holiday.items():
#         if "_holidays" in season:
#             filtered_holidays_season[season] = holidays
#     return filtered_holidays_season
#
#
# # Sorting the bank holidays from the api based on the
# # season and year that the user wants to go on holiday in
#
# def filter_by_year(filtered_season_result, year, season):
#     filtered_holidays_year = {}
#
#     for key, holidays_list in filtered_season_result.items():
#         season_key = key.replace("_holidays", "")
#         if season_key == holiday_season:
#             # filtered_holidays_year[season_key] = holidays_list
#             filter_by_year_season = [holiday for holiday in holidays_list if holiday["date"].startswith(year)]
#             filtered_holidays_year[season_key] = filter_by_year_season
#     return filtered_holidays_year
#
#
# # running and testing that the bank holidays based on the
# # user preferences have been filtered properly
# filtered_season_result = filtered_season()
# filtered_year_season = filter_by_year(filtered_season_result, holiday_year, holiday_season)
#
# date_list = [holiday["date"] for holiday in filtered_year_season[holiday_season]]
# date_obj_list = [datetime.strptime(date_str, "%Y-%m-%d") for date_str in date_list]
#
#
# date_list = [holiday["date"] for holiday in filtered_year_season[holiday_season]]
# date_obj_list = [datetime.strptime(date_str, "%Y-%m-%d") for date_str in date_list]
# #
#
# def calc_holiday_date():
#     holiday_results = []  # List to store holiday messages
#
#     for date_obj in date_obj_list:
#         hol_start = date_obj.date() - timedelta(days=2)
#         hol_end = hol_start + timedelta(days=days_of_holiday)
#         final_holiday = print("You will be on holiday from", hol_start, "till", hol_end)
#         if date_obj.weekday() == 0 or date_obj.weekday() == 4:  # 0 is Monday, 4 is Friday
#             return final_holiday
#         else:
#             holiday_results.append(final_holiday)
#
#     if not any(holiday_results):
#         # If no holidays are found, set hol_start on a Saturday in autumn
#         hol_start = datetime(year=int(holiday_year), month=9, day=1)
#         while hol_start.weekday() != 5:  # 5 is Saturday
#             hol_start += timedelta(days=1)
#         hol_end = hol_start + timedelta(days=days_of_holiday)
#         final_holiday = print("You will be on holiday from", hol_start.date(), "till", hol_end.date())
#         return final_holiday
#
# calc_holiday_date()