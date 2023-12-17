import random
from datetime import datetime, timedelta
from LeavePlannerLogic.Holiday_api import categorized_holiday


class RandomHolidayGenerator:
    def __init__(self, categorized_holiday):
        self.categorized_holiday = categorized_holiday

    def possible_holiday_dates(self):
        all_holidays = [holiday for holidays in self.categorized_holiday.values() for holiday in holidays]
        return [
            (datetime.strptime(holiday.get("date", "N/A"), "%Y-%m-%d").date(), holiday.get("title", "N/A"))
            for holiday in all_holidays
            if datetime.strptime(holiday.get("date", "N/A"), "%Y-%m-%d") > datetime.now()
        ]

    def random_hol_calc(self):
        all_holidays = self.possible_holiday_dates()

        random_holiday = random.choice(all_holidays)

        rand_holiday_start = random_holiday[0]  # getting date
        rand_holiday_title = random_holiday[1]  # getting title
        rand_holiday_length = random.randint(1, 15)
        rand_holiday_end = rand_holiday_start + timedelta(days=rand_holiday_length)

        return rand_holiday_start, rand_holiday_title, rand_holiday_length, rand_holiday_end

    def random_holiday_interaction(self):
        generate_holiday = True
        while True:
            try:
                user_answer = input(f"Do you want to generate a random holiday? (yes or no): ")
            except Exception as e:
                print(f"Exception occurred: {e}")
            if user_answer.lower() == "yes":
                result = self.random_hol_calc()
                print(
                    f"You will be going on a {result[1]} getaway for {result[2]} days, from {result[0]} till {result[3]}!")
                while True:
                    user_choice = input(
                        "Do you want to exit or continue with this program? (continue/exit): ")
                    if user_choice.lower() == "continue":

                        break
                    elif user_choice.lower() == "exit":
                        generate_holiday = False
                        break
                    else:
                        print("Please respond with either continue or exit.")
            elif user_answer.lower() == "no":
                break
            else:
                print("Please respond with yes or no.")
    def run(self):
        self.possible_holiday_dates()
        self.random_hol_calc()
        self.random_holiday_interaction()



# if __name__ == "__main__":
#     randomizer = RandomHolidayGenerator(categorized_holiday)
#     randomizer.random_holiday_interaction()
