from user_input import new_or_recurring
from LeavePlannerLogic.LeavePlanner import LeavePlannerFunc
from LeavePlannerLogic.API_Logic.Holiday_api import categorized_holiday, bank_holidays

print("""
 ____  __  __    _    ____ _____ _     _____    ___     _______ 
/ ___||  \/  |  / \  |  _ \_   _| |   | ____|  / \ \   / / ____|
\___ \| |\/| | / _ \ | |_) || | | |   |  _|   / _ \ \ / /|  _|  
 ___) | |  | |/ ___ \|  _ < | | | |___| |___ / ___ \ V / | |___ 
|____/|_|  |_/_/   \_\_| \_\|_| |_____|_____/_/   \_\_/  |_____|
            """)


# Retrieve user data from the database or add them as user
user_data = new_or_recurring()

# Ask user whether they need more from the app or do they want to quit.
user_choice = input("Do you need more help from SmartLeave today? Y/N: ")
if user_choice == 'y':
    print("""
    Options:
          Would you like to know:
            a) when the next bank holiday is?
            b) know what date options you have to maximise your annual leave this year?
            c) know when the quieter season is?
            d) Do I need to use AL to get my birthday off this year?
            e) lets the faiths decide when you should book your leave?
          """)
    next_step = input('Letter? ')
    if next_step.lower() == 'a':
        print("The next bank holiday is", LeavePlannerFunc.next_bank_holiday(bank_holidays))
    elif next_step.lower() == 'b':
        which_year = input('What would you like to use?')
    elif next_step.lower() == 'd':
        my_birthday = input('Please input your birthday in format mm-dd /n please include the year in which you are hoping to have off eg 2024-03-25: ')
        if not LeavePlannerFunc.birthday_off(my_birthday):
            print('Sorry')
        else:
            print('Yay')


elif user_choice == 'n':
    print("Goodbye - Have a wonderful day!")
else:
    print("Please try again and type either 'y' or 'n'. ")


# if __name__ == "__main__":
#     smart_leave_app = User_details()
#     smart_leave_app.get_user_name()
#     smart_leave_app.display_welcome_message()
