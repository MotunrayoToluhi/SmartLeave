from abc import abstractmethod

from user_input import new_or_recurring
from LeavePlannerLogic.LeavePlanner import LeavePlannerFunc
from LeavePlannerLogic.Holiday_api import bank_holidays, categorized_holiday
from LeavePlannerLogic.random_holiday import RandomHolidayGenerator
from LeavePlannerLogic.birthdayholiday import Birthday_next_bank_holiday


# Ask user whether they need more from the app or do they want to quit.


def user_intro_info():
    print("""
     ____  __  __    _    ____ _____ _     _____    ___     _______ 
    / ___||  \/  |  / \  |  _ \_   _| |   | ____|  / \ \   / / ____|
    \___ \| |\/| | / _ \ | |_) || | | |   |  _|   / _ \ \ / /|  _|  
     ___) | |  | |/ ___ \|  _ < | | | |___| |___ / ___ \ V / | |___ 
    |____/|_|  |_/_/   \_\_| \_\|_| |_____|_____/_/   \_\_/  |_____|
                """)

    # Retrieve user data from the database or add them as user
    user_data = new_or_recurring()


class SmartLeave:
    def __init__(self):
        user_intro_info()
        self.user_options = self.user_options()

    def user_options(self):

        # user_choice = input("Do you need more help from SmartLeave today? Y/N: ")
        # if user_choice == 'y':
        print("""
        Main menu:
              Would you like to:
                a) Know when the next bank holiday is?
                b) Get help maximizing your annual leave for your next holiday?
                c) Know which season has the least bank holidays?
                d) Know if your birthday is on a bank holiday this year?
                e) Lets the faiths decide when you should book your leave?
                f) Exit SmartLeave
              """)
        next_step = input("Letter?: ")
        if next_step.lower() == "a":
            print("The next bank holiday is", Birthday_next_bank_holiday.next_bank_holiday(bank_holidays))
            return self.user_options()

        elif next_step.lower() == "b":
            leave_planner = LeavePlannerFunc()
            leave_planner.run_leave_planner()
            return self.user_options()

        elif next_step.lower() == "d":
            my_birthday = input(
                "Please input your birthday in format mm-dd /n please include the year in which you are hoping to "
                "have off eg 2024-03-25: ")
            if not LeavePlannerFunc.birthday_off(my_birthday):
                print("Sorry")
            else:
                print("Yay")
            return self.user_options()

        elif next_step.lower() == "e":
            random = RandomHolidayGenerator(categorized_holiday=categorized_holiday)
            random.run()
            return self.user_options()
        elif next_step.lower() == "f":
            print("Goodbye - Have a wonderful day!")
            exit()
        else:
            print("Please try again and type either 'y' or 'n'. ")



if __name__ == "__main__":
    smart_leave_app = SmartLeave()
    # smart_leave_app.get_user_name()
    # smart_leave_app.display_welcome_message()
