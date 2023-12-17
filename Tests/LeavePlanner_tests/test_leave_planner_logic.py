import unittest.mock
from LeavePlannerLogic.LeavePlanner import leave_planner


class TestLeaveEntitlement(unittest.TestCase):
    def test_leave_entitlement_valid_number(self):
        # chose this test as it is a valid number
        with unittest.mock.patch('builtins.input', return_value='28'):
            result = leave_planner.leave_entitlement()
        self.assertEqual(result, 28, "Valid number test failed")

    def test_leave_entitlement_invalid_string(self):
        # chose this test as it is an invalid string
        with unittest.mock.patch('builtins.input', return_value='twenty'):
            result = leave_planner.leave_entitlement()
        self.assertIsNone(result, "Invalid string test failed")

    def test_leave_entitlement_invalid_boundary(self):
        # chose this test as it is an invalid boundary case
        with unittest.mock.patch('builtins.input', return_value='0'):
            result = leave_planner.leave_entitlement()
        self.assertIsNone(result, "Invalid boundary test failed")

    if __name__ == '__main__':
        unittest.main()

