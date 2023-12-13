class HolidayRequest:

    def __init__(self, season, total_days, annual_leave):
        self.season = season
        self.total_days = total_days
        self.annual_leave = annual_leave

    def confirm_request(self):
        return ("Let's check, you want to go on holiday in {}, for a total of {} days and using a maximum of {} days "
                "off? Answer 'y' or 'n'").format(self.season, self.total_days, self.annual_leave)


hol_request_1 = HolidayRequest("summer", 5, 2)

#print(hol_request_1.confirm_request())

# creating a class for handling members

class User:
    def __init__(self, user_name, user_total_al, user_remaining_al):
        self.user_name = user_name
        self.user_total_al = user_total_al
        self.user_remaining_al = user_remaining_al
#
#
# # use INSERT IGNORE to avoid duplicates in info
#     def add_user_to_db(self, user):
#         with self.connection.cursor() as cursor:
#             cursor.execute('''
#                 INSERT IGNORE INTO user_info (user_name, user_total_al, user_remaining_al)
#                 VALUES (%s, %s, %s)
#             ''', (user.user_name, user.user_total_al, user.user_remaining_al))
#             self.connection.commit()
#
#     def check_user_in_db(self, user):
#         with self.connection.cursor() as cursor :
#             cursor.execute('''
#             SELECT * FROM user_info WHERE user_name = %s
#             ''', (user.user_name))
#             return cursor.fetchone() is not None
#
#     def close_connection(self):
#         self.connection.close()
#
#
# if __name__ == "__main__":
#     # a user object
#     user_1 = User("Jane", 30, 25)
#
#     # creating user manager
#     user_manager = UserDatabase()
#
#     #attempt to add the new user to the db
#     user_manager.add_user_to_db(user_1)
#
#     #check if it worked and is in db
#     is_user_in_db = user_manager.check_user_in_db(user_1)
#     print(f"Is user in the database? {is_user_in_db}")
#
#     #close the connection
#     user_manager.close_connection()






