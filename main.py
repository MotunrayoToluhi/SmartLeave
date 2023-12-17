from abc import abstractmethod

from user_input import new_or_recurring
from LeavePlannerLogic.LeavePlanner import LeavePlannerFunc
from LeavePlannerLogic.Holiday_api import bank_holidays, categorized_holiday
from LeavePlannerLogic.random_holiday import RandomHolidayGenerator
from LeavePlannerLogic.OtherOptions import UserOptions


# Ask user whether they need more from the app or do they want to quit.
class SmartLeave:
    def __init__(self):
        self.user_intro_info = self.user_intro_info()
        self.user_options = self.user_options()

    def user_intro_info(self):
        print("""
         ____  __  __    _    ____ _____ _     _____    ___     _______ 
        / ___||  \/  |  / \  |  _ \_   _| |   | ____|  / \ \   / / ____|
        \___ \| |\/| | / _ \ | |_) || | | |   |  _|   / _ \ \ / /|  _|  
         ___) | |  | |/ ___ \|  _ < | | | |___| |___ / ___ \ V / | |___ 
        |____/|_|  |_/_/   \_\_| \_\|_| |_____|_____/_/   \_\_/  |_____|
                    """)

        # Retrieve user data from the database or add them as user
        user_data = new_or_recurring()


    def user_options(self):

        # user_choice = input("Do you need more help from SmartLeave today? Y/N: ")
        # if user_choice == 'y':
        print("""
        Main menu:
              Would you like to:
                a) Know when the next bank holiday is?
                b) Know when the closest together bank holidays are next year?
                c) Get help maximizing your annual leave for your next holiday?
                c) Prevent burnout by knowing which season has the least bank holidays?
                d) Know if your birthday is on a bank holiday or weekend this year?
                e) Lets the faiths decide when you should book your leave?
                f) Exit SmartLeave
              """)
        next_step = input("Letter?: ")
        if next_step.lower() == "a":
            print("The next bank holiday is", UserOptions.next_bank_holiday(bank_holidays))
            return self.user_options()
        elif next_step.lower() == "b":
            print("The closet together bank holidays next year are:", )

            return self.user_options()

        elif next_step.lower() == "c":
            LeavePlannerFunc()
            # print("yes")  # test to see if while true works by itself
            while True:
                user_choice = input(
                    "Do you want to exit or continue with this program? (continue/exit): ")
                if user_choice.lower() == "continue":
                    LeavePlannerFunc()
                    break
                elif user_choice.lower() == "exit":
                    self.user_options()
                    break
                else:
                    print("Please respond with either continue or exit.")
        elif next_step.lower() == "c":
            print("There are no bank holidays in autumn. We suggest you consider booking your holiday in another "
                  "season.")
            return self.user_options()

        elif next_step.lower() == "d":
            my_birthday = input(
                "Please input your birthday in format mm-dd, please include the year in which you are hoping to "
                "have off eg 2024-03-25: ")
            if not UserOptions.birthday_off(my_birthday):
                print("Sorry, you're birthday does not land on a bank holiday or weekend.")
            else:
                print("Yay - no need use Annual Leave. Your birthday lands on either a bank holiday or weekend.")
            return self.user_options()
        elif next_step.lower() == "e":
            random = RandomHolidayGenerator(categorized_holiday=categorized_holiday)
            RandomHolidayGenerator.random_holiday_interaction(random)
            return self.user_options()
        elif next_step.lower() == "f":
            print("Goodbye - Have a wonderful day!")
            exit()
        else:
            print("Please try again and type either 'y' or 'n'. ")


if __name__ == "__main__":
    smart_leave_app = SmartLeave()
