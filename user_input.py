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
