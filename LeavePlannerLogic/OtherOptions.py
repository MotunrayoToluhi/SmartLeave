import datetime
from Final_project.LeavePlannerLogic.Holiday_api import bank_holidays


class UserOptions:

    def __init__(self):
        self.birthday = self.birthday_off()
        self.next_bank = self.next_bank_holiday()

    # function to get next bank holiday
    def next_bank_holiday(bank_hol):
        today = datetime.datetime.now().date()
        next_one = min(bank_holidays, key=lambda x: abs(x - today))
        return next_one

    # function check if birthday lands on weekend or AL or neither
    def birthday_off(birthday):
        date_birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d').date()
         # print(date_birthday)
        bday_hol = any(date_birthday == num for num in bank_holidays)
        # print(bday_hol)
        if not bday_hol:
            if date_birthday.weekday() >= 5:
                return True
            elif date_birthday.weekday() < 5:
                return False
        else:
            return True

    # gets 2 bank holidays with the shortest time between them
    def close_bank_hols(listofbankhols, year):
        next_year = int(year) + 1
        the_year = datetime.datetime.strptime(year, '%Y').date()
        next_year = datetime.datetime.strptime(str(next_year), '%Y').date()
        this_years_bank_hols = [date for date in listofbankhols if the_year <= date <= next_year]
        # print(this_years_bank_hols)
        # getting the length of time between bank holidays
        l = len(this_years_bank_hols)
        seven_days = datetime.timedelta(days=7)
        for i in range(l):
            for x in range(i + 1, l):
                days = this_years_bank_hols[x] - this_years_bank_hols[i]
                if days <= seven_days:
                    int_days = days.days
                    return int_days, str(this_years_bank_hols[x]), str(this_years_bank_hols[i])


# UserOptions.close_bank_hols(bank_holidays, '2024')

closet = UserOptions.close_bank_hols(bank_holidays, '2024')
print(f"The closet together bank holidays in the next year are: {closet[1]} and {closet[2]} with {closet[0]} days between.")
