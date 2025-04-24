import pandas as pd
import datetime

a = pd.Timestamp("2024-01-15")
print("Date time object for Jan 15 2012:", a)

b= pd.Timestamp("2005-07-12 21:20:00")
print("Specific date and time of 9:20 pm:", b)


c = pd.Timestamp.now()
print("Local date and time:", c)


d = pd.Timestamp("2005-07-12").date()
print("A date without time:", d)


e = pd.Timestamp.today().date()
print("Current date:", e)


f = pd.Timestamp("2005-07-12 21:20:00").time()
print("Time from a date time:", f)


g = datetime.datetime.now().time()
print("Current local time:", g)
