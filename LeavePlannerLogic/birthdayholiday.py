import datetime
from LeavePlannerLogic.Holiday_api import categorized_holiday, bank_holidays

class Birthday_next_bank_holiday:
    def __init__(self):
        self.next_bank = self.next_bank_holiday()
        self.birthday = self.birthday_off()

    def next_bank_holiday(bank_hol):
        today = datetime.datetime.now().date()
        next_one = min(bank_holidays, key=lambda x: abs(x - today))
        return next_one

    # function check if birthday lands on weekend or AL or neither
    def birthday_off(birthday):
        date_birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d').date()
        print(date_birthday)
        bday_hol = any(date_birthday == num for num in bank_holidays)
        print(bday_hol)
        if bday_hol == False:
            if date_birthday.weekday() >= 5:
                return True
            elif date_birthday.weekday() < 5:
                return False
        else:
            return True

    # need to re-write this in to __init__
    def maximise(listofbankhols, year):
        # getting just that years holidays plus new years day
        next_year = int(year) + 1
        the_year = datetime.datetime.strptime(year, '%Y').date()
        next_year = datetime.datetime.strptime(str(next_year), '%Y').date()
        this_years_bank_hols = [date for date in listofbankhols if the_year <= date <= next_year]
        time_differences = []
        # getting the lenght of time between bank holidays
        l = len(this_years_bank_hols)
        seven_days = datetime.timedelta(days=7)
        for i in range(l):
            for x in range(i + 1, l):
                days = this_years_bank_hols[x] - this_years_bank_hols[i]
                # get all bank holidays that have less than a week between them
                if days <= seven_days:
                    return (days, this_years_bank_hols[x], this_years_bank_hols[i])
                # print(this_years_bank_hols[x], this_years_bank_hols[i], days)

    # print(maximise(bank_holidays, '2024'))