from Database.Db_utils import get_user_info, add_user_to_db, update_used_al
from UserInfo.user_object import User


class UserInputs:
    def __init__(self):
        self.new_or_recurring = self.new_or_recurring()
        self.further_options = self.further_options()
        self.time_off_email = self.time_off_email()

    def new_or_recurring(self):
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
            if new_user_all_al > new_user_al_left:
                print('Your annual leave calculations are incorrect.\nYou cannot have more leave left than leave allocation\nLet\'s start again. ')
                UserInputs.new_or_recurring(self)
            else:
                user_data = User(new_user_name, new_user_all_al, new_user_al_left)
                add_user_to_db(user_data)
                print(f"You originally had {new_user_all_al} days of annual leave. You currently have {new_user_al_left} days remaining.")
                return user_data
        else:
            print("Your data is not recognise, please try again.")
            UserInputs.new_or_recurring(self)
            return

    # gives option to change db
    def further_options(self):
        update = input('Would you like to book any days off? Y/N: ')
        if update.lower() == 'yes' or update.lower() == 'y':
            user_name = input('Please confirm your name: ')
            user_data = get_user_info(user_name)
            remaining_al = user_data[3]
            print(f"You currently have {remaining_al} days of annual leave remaining.")
            day_change = input('How many days would you like to book?: ')
            new_remaining_al = remaining_al - int(day_change)
            update_used_al(user_name, new_remaining_al)
            print(f"You have updated our records, you now have {new_remaining_al} days of annual leave remaining.")
            email = input('Would you like a template email to send your manager? Y/N:')
            if email.lower() == 'yes' or email.lower() == 'y':
                date_from = input('What will be your start date? ')
                date_to = input('What will be your end date? ')
                UserInputs.time_off_email(self, day_change, date_from, date_to, new_remaining_al, user_name)
            else:
                return
        elif update.lower() == 'no' or update.lower() == 'n':
            return

    # write txt file for email template
    def time_off_email(self, number_of_days, date_one, date_two, now_remaining_al, name):
        with open('dear_manager.txt', 'w+') as manager_email:
            manager_email.write(
                f'''
              Dear Sir/Madam,
              
              I wish to request off {number_of_days} from {date_one} to {date_two}.
              These should leave me with {now_remaining_al} days of annual leave remaining..
    
              Kind Regards,
              {name}.
              '''
            )


