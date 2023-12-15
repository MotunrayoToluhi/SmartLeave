from Final_project.config import HOST, USER, PASSWORD
import mysql.connector
from Final_project.classes_file import User


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


# add user to  database
def select_all_userinfo():
    try:
        db_name = "SmartLeave"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        # print("Connected to DB")

        query = "SELECT * from user_info"

        cur.execute(query)

        result = cur.fetchall()

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data")

    finally:
        if db_connection:
            db_connection.close()
            # print("DB connection is closed")

    return result


# function to add users to the database

def add_user_to_db(user):
    try:
        db_name = "SmartLeave"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        # print("Connected to DB")

        cur.execute('''
                INSERT IGNORE INTO user_info (user_name, user_total_al, user_remaining_al)
               VALUES (%s, %s, %s)
            ''', (user.user_name, user.user_total_al, user.user_remaining_al))

        # commit the changes to the db
        db_connection.commit()
        print(f"Member {user.user_name} added to the database.")

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data")

    finally:
        if db_connection:
            db_connection.close()
            # print("DB connection is closed")


# function to get user info from the database
def get_user_info(user):
    try:
        db_name = "SmartLeave"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        # print("Connected to DB")

        cur.execute(''' SELECT * FROM user_info WHERE user_name = %s ''', (user,))
        user_info = cur.fetchone()

        # print(type(user_info[0]))
        # print(user_info)

        cur.close()
        return user_info


    except Exception:
        raise DbConnectionError("Failed to read data")

    finally:
        if db_connection:
            db_connection.close()
            # print("DB connection is closed")


# test if it works with this sample usage

if __name__ == "__main__":
    # trial user object
    user1 = User("Jane", 30, 25)
    user2 = User("Terri", 30, 25)

    # add_user_to_db(user2)
    # print(select_all_userinfo())

# me = get_user_info('Mari')
# print(me)
# print(type(me[0]))
# remaining = me[-1] - me[-2]
# print(remaining)
