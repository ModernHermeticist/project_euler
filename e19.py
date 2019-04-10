# 1 January 1900 was a Monday
# Leap year occurs on year divisible by 4, but not on a century unless divisible by 400
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
months = { "January": 31,
                   "February": 28,
                   "March": 31,
                   "April": 30,
                   "May": 31,
                   "June": 30,
                   "July": 31,
                   "August": 31,
                   "September": 30,
                   "October": 31,
                   "November": 30,
                   "December": 31 }

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
sundays = 0
day = 0
for year in range(1901, 2001):
    for month in months:
        if year % 4 == 0 and month == "February":
            for i in range(1, 30):
                print(str(days_of_week[day]) + ", " + month + " " + str(i) + ", " + str(year))
                day += 1
                if day == 6 and i == 1: sundays += 1
                if day == 7: day = 0
        else:
            for i in range(1, months.get(month)+1):
                print(str(days_of_week[day]) + ", " + month + " " + str(i) + ", " + str(year))
                day += 1
                if day == 6 and i == 1: sundays += 1
                if day == 7: day = 0

print(sundays)