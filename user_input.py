# def get_user_name():
#     name = input("Welcome to SmartLeave! What's your name? ")
#
#     return name

#
# class SmartLeaveApp:
#     def __init__(self):
#         self.user_name = ""
#
#     def get_user_name(self):
#         self.user_name = input("Welcome to SmartLeave! What's your name? ")

from Database.Db_utils import get_user_info, add_user_to_db
from classes_file import User

def new_or_recurring():
    # if user is in the db, get their info. If not, add their info
    print('Welcome to SmartLeave!')
    db_or_not_db = input('Have you used this app before? Y/N ')
    # get current users info
    if db_or_not_db.lower() == 'y' or db_or_not_db.lower() == 'yes':
        user_name = input("Welcome to back! What's your name? ")
        # try and except NoneType, means person is not already in DB
        try:
            user_data = get_user_info(user_name)
            total_al = user_data[2]
            remaining_al = user_data[3]
            # Display the user's original total and remaining annual leave
            print(f"You originally had {total_al} days of annual leave. You currently have {remaining_al} days remaining.")
            return user_data
        except Exception:
            raise TypeError('Your data is not recognise; please check you spelling or start again')
    # add new user to db
    elif db_or_not_db.lower() == 'n' or db_or_not_db.lower() == 'no':
        print('Welcome to easier holiday planning, please enter your required info:')
        new_user_name = input('What is your name? ')
        new_user_all_al = input('What is your allocation of annual leave? ')
        new_user_al_left = input('How many days of annual leave do you have left? ')
        try:
            if new_user_all_al < new_user_al_left:
                raise Exception
            user_data = User(new_user_name, new_user_all_al, new_user_al_left)
            add_user_to_db(user_data)
            print(f"You originally had {new_user_all_al} days of annual leave. You currently have {new_user_al_left} days remaining.")
            return user_data
        except:
            print('Your annual leave calculations are incorrect:\nYou cannot have more leave left than leave allocation' )
    else:
        print("Please input your name using letters only")
        return get_user_name()
    return name
# get_user_name()



