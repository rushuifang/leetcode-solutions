class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        if not self.calendar:
            self.calendar.append([start, end])
            return True
        
        for i in range(len(self.calendar)):
            if self.calendar[i][1] <= start and (i == len(self.calendar) - 1 or self.calendar[i + 1][0] >= end):
                self.calendar.insert(i + 1, [start, end])
                return True
            elif i == 0 and self.calendar[i][0] >= end:
                self.calendar.insert(i, [start, end])
                return True
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)