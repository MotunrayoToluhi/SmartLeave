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