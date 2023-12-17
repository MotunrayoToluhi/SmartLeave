def get_user_name():
    name = input("Welcome to SmartLeave! What's your name? ")
    
    return name


class SmartLeaveApp:
    def __init__(self):
        self.user_name = ""

    def get_user_name(self):
        self.user_name = input("Welcome to SmartLeave! What's your name? ")

    def display_welcome_message(self):
        print(f"Hello, {self.user_name}!")
       
    if name.isalpha():
        pass
    else:
        print("Please input your name using letters only")
        return get_user_name()
    return name
get_user_name()


# class User:
#
#     def __init__(self, name, all_annual_leave, used_days):
#         self.name = name
#         self.all_annual_leave = all_annual_leave
#         self.used_days = used_days
#
#
# def intro():
#     print('Welcome to SmartLeave!')
#     name = input('What is your name? ')
#     al = int(input('How many annual leave days do you have? '))
#     used_days = int(input('How many annual leave days have you used? '))
#     our_user = User(name, al, used_days)
#     remaining_al = al - used_days
#     print(f"You originally had {al} days of annual leave. You currently have {remaining_al} days remaining.")
#     return our_user


