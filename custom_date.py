class Date:
    # Constructor initializes the state of new Date objects as they are created by client code.
    # Raises a ValueError if values are out of range.
    def __init__(self, month, day, year):
        self.set_date(month, day, year)

    # Returns a string representation of a Date, such as "9/19".
    def __str__(self):
        return str(self._month) + "/" + str(self._day) + "/" + str(self._year)
    
    @property
    def  year(self):
        return self._is_leap_year() 

    @property
    def month(self):
        return self._month
    
    @property
    def absolute_day(self):
        return  self._calculate_absolute_day()

    @month.setter
    def month(self, value):
        self.set_date(value, self._day, self._year)

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self.set_date(self._year, self._month , value)

    # Advances the Date's state to the next day, wrapping into the next month/year as necessary.
    def advance(self):
        self._day += 1
        if self._day > self.days_in_month():  # Wrap to next month if day exceeds days in month
            self._month += 1
            self._day = 1
            if self._month > 12:  # Wrap to next year if month exceeds 12
                self._month = 1
                self._year += 1
              

    # Returns the number of days in this Date's month.
    def days_in_month(self):
        if self._month in {4, 6, 9, 11}:  
            return 30
        elif self._month == 2:  
            return 28
        else:
            return 31  

    # Modifies the date's month and day state.
    # Raises a ValueError if values are out of range.
    def set_date(self, month, day, year):
        if 1 <= month <= 12:
            self._month = month
        else:
            raise ValueError("Invalid month: " + str(month))
        
        if 1 <= day <= self.days_in_month():
            self._day = day
        else:
            raise ValueError("Invalid day: " + str(day))
        
        if len(int(year)) != 4: 
            raise ValueError("Invalid year: " + str(year))
        
        
    def _calculate_absolute_day(self):
        days_up_to_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        return days_up_to_month[self._month - 1] + self._day    
    
    
       
    def shift(self, days):
        self._day += days
        while self._day > self.days_in_month():
            self._day -= self.days_in_month()
            self._month +=1
            if self._month > 12:
                self._month = 1 

        while self._day <1:  
            self._month -=1
            if self._month <1 :    
                self._month = 12
            self._day += self.days_in_month()    
            
    def _is_leap_year(self) :
            return  self._year % 4 ==0 and  (self._year % 100 !=0 or self._year % 400 ==0) 
                







































