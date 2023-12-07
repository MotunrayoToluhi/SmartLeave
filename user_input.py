def get_user_name():
    name = input("Welcome to SmartLeave! What's your name? ")
    if name.isalpha():
        pass
    else:
        print("Please input your name using letters only")
        return get_user_name()
    return name
get_user_name()