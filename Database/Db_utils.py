import mysql.connector
from Final_project.classes_file import User
# from Final_project.Database.config import HOST, USER, PASSWORD

HOST = "127.0.0.1"
USER = "root"
PASSWORD = ""
PORT = "3306"
DATABASE = "SmartLeave"

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
        user_info= cur.fetchone()

        print(user_info)

        cur.close()

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

    # get_user_info('Ayo')


