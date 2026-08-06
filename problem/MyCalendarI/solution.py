class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        slotAvailable = True
        for i in self.calendar:
            if i[0] < end and i[1] > start:
                slotAvailable = False
                break
        if slotAvailable:
            self.calendar.append([start, end])
        return slotAvailable


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
# param_1 = obj.book(start, end)
print(obj.book(10, 20))  # returns true
print(obj.book(15, 25))  # returns false
print(obj.book(20, 30))  # returns true
print(obj.book(15, 10))  # returns true
