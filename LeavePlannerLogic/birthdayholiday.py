import datetime

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