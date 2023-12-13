from config import USER, PASSWORD, PORT, HOST
import mysql.connector


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


# Try out helper option
def get_user_data_by_name(current_name):
    try:
        db_name = "SmartLeave"
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        # print("Connected to DB")

        query = "SELECT user_total_al, user_remaining_al FROM user_info WHERE user_name = %s"

        cur.execute(query, current_name)

        result = cur.fetchall()

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data")

    finally:
        if db_connection:
            db_connection.close()
            # print("DB connection is closed")

    return result


current_name = 'Ayo'
get_user_data_by_name(current_name)

