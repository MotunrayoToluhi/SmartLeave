class HolidayRequest:

    def __init__(self, season, total_days, annual_leave):
        self.season = season
        self.total_days = total_days
        self.annual_leave = annual_leave

    def confirm_request(self):
        return ("Let's check, you want to go on holiday in {}, for a total of {} days and using a maximum of {} days "
                "off? Answer 'y' or 'n'").format(self.season, self.total_days, self.annual_leave)


hol_request_1 = HolidayRequest("summer", 5, 2)

print(hol_request_1.confirm_request())

