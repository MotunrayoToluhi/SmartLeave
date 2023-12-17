import random
from datetime import datetime, timedelta
from Final_project.LeavePlannerLogic.Holiday_api import categorized_holiday


class RandomHolidayGenerator:
    def __init__(self, categorized_holiday):
        self.categorized_holiday = categorized_holiday

    #creating list for holidays that can be picked as a random holiday
    def possible_holiday_dates(self):
        all_holidays = [holiday for holidays in self.categorized_holiday.values() for holiday in holidays]
        return [
            (datetime.strptime(holiday.get("date", "N/A"), "%Y-%m-%d").date(), holiday.get("title", "N/A"))
            for holiday in all_holidays
            if datetime.strptime(holiday.get("date", "N/A"), "%Y-%m-%d") > datetime.now()
        ]

    # calculates a random holiday from the list
    def random_hol_calc(self):
        all_holidays = self.possible_holiday_dates()

        random_holiday = random.choice(all_holidays)

        rand_holiday_start = random_holiday[0]  # getting date
        rand_holiday_title = random_holiday[1]  # getting title
        rand_holiday_length = random.randint(1, 15)
        rand_holiday_end = rand_holiday_start + timedelta(days=rand_holiday_length)

        return rand_holiday_start, rand_holiday_title, rand_holiday_length, rand_holiday_end

    #user interacction thet tels user what random holiday they should go on
    def random_holiday_interaction(self):
            try:
                user_answer = input(f"Do you want to generate a random holiday? (yes or no): ")
            except Exception as e:
                print(f"Exception occurred: {e}")
            if user_answer.lower() == "yes":
                result = self.random_hol_calc()
                print(
                    f"You will be going on a {result[1]} getaway for {result[2]} days, from {result[0]} till {result[3]}!")

            elif user_answer.lower() == "no":
                return
            else:
                print("Please respond with yes or no.")


if __name__ == "__main__":
    randomizer = RandomHolidayGenerator(categorized_holiday)
    randomizer.random_holiday_interaction()
