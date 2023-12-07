from user_input import get_user_name
from Database.Db_utils import get_user_data_by_name

# Get user input
user_name = get_user_name()

# Retrieve user data from the database
user_data = get_user_data_by_name(user_name)

# Organise data into total annual leave and remaining
total_al = user_data[0][0]
remaining_al = user_data[0][1]

# Display the user's original total and remaining annual leave
print(f"You originally had {total_al} days of annual leave. You currently have {remaining_al} days remaining.")

# Ask user whether they need more from the app or do they want to quit.
user_choice = input("Do you need more help from SmartLeave today? Answer 'y' or 'n': ")
if user_choice == 'y':
    print("Yes")
elif user_choice == 'n':
    print("No")
else:
    print("Please try again and type either 'y' or 'n'. ")