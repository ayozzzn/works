# Python Datetime.
# Import the datetime module and display the current date :
import datetime
x = datetime.datetime.now()
print(x)

# Return the year and name of weekday :
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

# Creating Date Objects.
# The datetime() class requires three parameters to create a date: year, month, day.
# Create a date object :
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)

# The strftime() Method.
# Display the name of the month :
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

# %a - weekday, short version. Example : Wed.
# %A - weekday, full version. Example : Wednesday.
# %w - weekday as a number 0-6, 0 is Sunday. Example : 3.
# %d - day of month 01-31. Example : 31.
# %b - month name, short version. Example : Dec.
# %B - month name, full version. Example : December.
# %m - month as number 01-12. Example : 12.
# %y - year, short version, without century. Example : 18.
# %Y - year, full version. Example : 2018.
# %H - hour 00-23. Example : 17.
# %I - hour 00-12. Example : 05.
# %p - AM/PM. Example : PM.
# %M - minute 00-59. Example : 41.
# %S - second 00-59. Example : 08.
