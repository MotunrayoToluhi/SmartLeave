import unittest
from Database.Db_utils import get_user_info, DbConnectionError


class TestUserInfo(unittest.TestCase):
    def test_get_user_info_valid_user(self):
        # Chose this test as the user exists in the database
        user_info = get_user_info("kate")
        self.assertIsNotNone(user_info)

    def test_get_user_info_invalid_user(self):
        # Chose this test as the user doesn't exist in the database
        with self.assertRaises(DbConnectionError):
            get_user_info("Hannah")

    def test_get_user_info_boundary_case(self):
        # Chose this test as the input is at the lower end of expected length
        user_info = get_user_info("a" * 1)
        self.assertIsNotNone(user_info)


if __name__ == '__main__':
    unittest.main()
