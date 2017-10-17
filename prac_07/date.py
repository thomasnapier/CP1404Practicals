MONTH_THRESHOLD = 30
class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "{}/{}/{}".format(self.day, self.month, self.year)

    def add_days(self, days):
        self.day += days
        while self.day >= MONTH_THRESHOLD:
            self.day -= MONTH_THRESHOLD
            self.month += 1
            if self.month > 12:
                self.month = 0
                self.year += 1
