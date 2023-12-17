from UserInfo.user_input import UserInputs
from LeavePlannerLogic.LeavePlanner import LeavePlannerFunc
from LeavePlannerLogic.Holiday_api import bank_holidays, categorized_holiday
from LeavePlannerLogic.random_holiday import RandomHolidayGenerator
from LeavePlannerLogic.OtherOptions import UserOptions


# SmartLeave inherits from UserInputs in the user_input file
class SmartLeave(UserInputs):
    def __init__(self):
        self.user_intro_info = self.user_intro_info()
        self.user_options = self.user_options()
        super().__init__()

    def user_intro_info(self):
        print("""
         ____  __  __    _    ____ _____ _     _____    ___     _______ 
        / ___||  \/  |  / \  |  _ \_   _| |   | ____|  / \ \   / / ____|
        \___ \| |\/| | / _ \ | |_) || | | |   |  _|   / _ \ \ / /|  _|  
         ___) | |  | |/ ___ \|  _ < | | | |___| |___ / ___ \ V / | |___ 
        |____/|_|  |_/_/   \_\_| \_\|_| |_____|_____/_/   \_\_/  |_____|
                    """)

        # Retrieve user data from the database or add them as user
        user_data = UserInputs.new_or_recurring(self)

    def user_options(self):

        print("""
        Main menu:
              Would you like to:
                a) Know when the next bank holiday is?
                b) Know when the closest together bank holidays are?
                c) Get help maximizing your annual leave for your next holiday?
                d) Prevent burnout by knowing which season has the least bank holidays?
                e) Know if your birthday is on a bank holiday or weekend this year?
                f) Lets the faiths decide when you should book your leave?
                g) Exit SmartLeave
              """)
        next_step = input("Letter?: ")

        if next_step.lower() == "a":
            print("The next bank holiday is", UserOptions.next_bank_holiday(bank_holidays))
            return self.user_options()
        elif next_step.lower() == "b":
            year = input('For which year: 2023, 2024 or 2025? ')
            closet = UserOptions.close_bank_hols(bank_holidays, year)
            print(f"The closet together bank holidays in the next year are: {closet[1]} and {closet[2]} with {closet[0]} days between.")
            UserInputs.further_options(self)
            return self.user_options()

        elif next_step.lower() == "c":
            leave_planner = LeavePlannerFunc()
            your_holiday = leave_planner.leave_days_used()
            UserInputs.further_options(self)
            return your_holiday, self.user_options()

        elif next_step.lower() == "d":
            print("There are no bank holidays in autumn. We suggest you consider booking your holiday in another "
                "season.")
            return self.user_options()

        elif next_step.lower() == "e":
            my_birthday = input(
                "Please input your birthday in format mm-dd, please include the year in which you are hoping to "
                "have off eg 2024-03-25: ")
            if not UserOptions.birthday_off(my_birthday):
                print("Sorry, you're birthday does not land on a bank holiday or weekend.")
            else:
                print("Yay - no need use Annual Leave. Your birthday lands on either a bank holiday or weekend.")
            UserInputs.further_options(self)
            return self.user_options()

        elif next_step.lower() == "f":
            random = RandomHolidayGenerator(categorized_holiday=categorized_holiday)
            RandomHolidayGenerator.random_holiday_interaction(random)
            UserInputs.further_options(self)
            return self.user_options()

        elif next_step.lower() == "g":
            print("Goodbye - Have a wonderful day!")
            exit()
        else:
            print("Please try again and type either 'y' or 'n'. ")


if __name__ == "__main__":
    smart_leave_app = SmartLeave()
