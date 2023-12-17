from datetime import datetime, timedelta
import numpy
from LeavePlannerLogic.API_Logic.Holiday_api import categorized_holiday



# Functionality for leave planner
# tells the user:
# what dates they should go on holiday on based on bank holidays
# how many leave days were used
# how many days were saves

class LeavePlannerFunc:

    def __init__(self):
        # self.next_bank = self.next_bank_holiday()
        # self.birthday = self.birthday_off()
        self.max_leave = self.leave_entitlement()
        self.days_of_holiday = self.holiday_length()
        self.holiday_year = self.user_chosen_year()
        self.holiday_season = self.user_chosen_season()
        self.filtered_season_result = self.filtered_season()
        self.filtered_year_season = self.filter_by_year(
            self.filtered_season_result, self.holiday_year, self.holiday_season
        )
        self.date_list = [holiday["date"] for holiday in self.filtered_year_season[self.holiday_season]]

        self.date_obj_list = [datetime.strptime(date_str, "%Y-%m-%d") for date_str in self.date_list]
        self.calc_holiday_date()
        self.date_obj_list = [datetime.datetime.strptime(date_str, "%Y-%m-%d") for date_str in self.date_list]


    # function to get next bank holiday
    # def next_bank_holiday(bank_hol):
    #     today = datetime.datetime.now().date()
    #     next_one = min(bank_holidays, key=lambda x: abs(x - today))
    #     return next_one
    #
    # # function check if birthday lands on weekend or AL or neither
    # def birthday_off(birthday):
    #     date_birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d').date()
    #     print(date_birthday)
    #     bday_hol = any(date_birthday == num for num in bank_holidays)
    #     print(bday_hol)
    #     if bday_hol == False:
    #         if date_birthday.weekday() >= 5:
    #             return True
    #         elif date_birthday.weekday() < 5:
    #             return False
    #     else:
    #         return True
    #
    # # need to re-write this in to __init__
    # def maximise(listofbankhols, year):
    #     # getting just that years holidays plus new years day
    #     next_year = int(year) + 1
    #     the_year = datetime.datetime.strptime(year, '%Y').date()
    #     next_year = datetime.datetime.strptime(str(next_year), '%Y').date()
    #     this_years_bank_hols = [date for date in listofbankhols if the_year <= date <= next_year]
    #     time_differences = []
    #     # getting the lenght of time between bank holidays
    #     l = len(this_years_bank_hols)
    #     seven_days = datetime.timedelta(days=7)
    #     for i in range(l):
    #         for x in range(i + 1, l):
    #             days = this_years_bank_hols[x] - this_years_bank_hols[i]
    #             # get all bank holidays that have less than a week between them
    #             if days <= seven_days:
    #                 return (days, this_years_bank_hols[x], this_years_bank_hols[i])
                # print(this_years_bank_hols[x], this_years_bank_hols[i], days)

    # print(maximise(bank_holidays, '2024'))


    # asks user max leave entitlement they have
    def leave_entitlement(self):
        while True:
            self.max_leave = input(f"How many leave days are you entitled to per year?: ")
            if self.max_leave.isdigit():
                self.max_leave = int(self.max_leave)
                if 0 < self.max_leave < 365:
                    break
                else:
                    print("Days must be more than zero and less than 365.")
            else:
                print(f"Please enter valid positive a number.")
        return self.max_leave

    # asks user what season they want to go on holiday in
    def user_chosen_season(self):
        while True:
            preferred_season = input(f"What do you want to go on holiday in? (Winter, Spring, Summer, Autumn): ")
            preferred_season = preferred_season.lower()
            if preferred_season in ["winter", "spring", "summer", "autumn"]:
                break
            else:
                print("Season must be Summer, Winter, Spring, or Autumn")
        return preferred_season

    # asks user what year they want tot go on holiday in
    def user_chosen_year(self):
        while True:
            preferred_year = input(f"What do you year to go on holiday in? (2023, 2024, 2025): ")
            preferred_year = preferred_year.lower()
            if preferred_year in ["2023", "2024", "2025"]:
                break
            else:
                print("year must be 2023, 2024 or 2025")
        return preferred_year

    # asks user how many days notice they need to give their employer before booking a holiday
    #     def days_notice(self):
    #         while True:
    #             user_days_notice = input(f"How many days notice do you need to give your employer?: ")
    #             if user_days_notice.isdigit():
    #                 user_days_notice = int(user_days_notice)
    #                 if 0 < user_days_notice < 365:
    #                     break
    #                 else:
    #                     print("Days must be more than zero and less than 365.")
    #             else:
    #                 print(f"Please enter a valid positive number.")
    #         return user_days_notice

    # asks user how long they want their holiday to be
    def holiday_length(self):
        while True:
            self.user_hol_len = input(f"How many days do you want to be on holiday for?: ")
            if self.user_hol_len.isdigit():
                self.user_hol_len = int(self.user_hol_len)
                if 0 < self.user_hol_len <= self.max_leave:
                    break
                else:
                    print("Please input a number less than the total leave days you are entitled to.")
            else:
                print(f"Please enter a valid positive number.")
        return self.user_hol_len

    # filters possible bank holidays user van go on holiday in based on season they chose
    def filtered_season(self):
        filtered_holidays_season = {}
        for season, holidays in categorized_holiday.items():
            if "_holidays" in season:
                filtered_holidays_season[season] = holidays
        return filtered_holidays_season

    # filters possible bank holidays user van go on holiday in based on season and year they chose
    def filter_by_year(self, filtered_season_result, year, season):
        filtered_holidays_year = {}
        for key, holidays_list in filtered_season_result.items():
            season_key = key.replace("_holidays", "")
            if season_key == season:
                filter_by_year_season = [holiday for holiday in holidays_list if holiday["date"].startswith(year)]
                filtered_holidays_year[season_key] = filter_by_year_season
        return filtered_holidays_year

    # calculates date range for when the user goes on holiday based on their preferences
    def calc_holiday_date(self):
        holiday_results = []

        for date_obj in self.date_obj_list:
            hol_start = date_obj.date() - timedelta(days=2)
            hol_end = hol_start + timedelta(days=self.days_of_holiday)
            final_holiday = (hol_start, hol_end)

            if date_obj.weekday() == 0 or date_obj.weekday() == 4:  # 0 is Monday, 4 is Friday
                return final_holiday
            else:
                holiday_results.append(final_holiday)

        if not any(holiday_results):
            hol_start = datetime(year=int(self.holiday_year), month=9, day=1)
            while hol_start.weekday() != 5:  # 5 is Saturday
                hol_start += timedelta(days=1)
            hol_end = hol_start + timedelta(days=self.days_of_holiday)

            return hol_start, hol_end


    # calculates the leave days used and saved if user books this holiday off
    # tells user the date range they should use for their holiday and how many leave days they used and saves
    def leave_days_used(self):
        holiday_range = self.calc_holiday_date()

        if holiday_range:
            hol_start, hol_end = holiday_range

            print("You will be going on a", self.days_of_holiday, "day holiday from", hol_start, "till", hol_end, "!")
            if self.holiday_season.lower() == "autumn":
                hol_start = hol_start.astype("<M8[D]")
                hol_end = hol_end.astype("<M8[D]")
                leave_days_used = numpy.busday_count(hol_start, hol_end)
                leave_saved = self.days_of_holiday - leave_days_used
                print("You have used", leave_days_used, "leave days and have saved", leave_saved, "days")
            elif self.holiday_season.lower() != "autumn":
                leave_days_used = numpy.busday_count(hol_start, hol_end) - 1
                leave_saved = self.days_of_holiday - leave_days_used
                print("You have used", leave_days_used, "leave days and have saved", leave_saved, "days")


# runs program
if __name__ == "__main__":
    leave_planner = LeavePlanner()
    leave_planner.leave_days_used()
