from datetime import *

dob_str = "24-10-1998"

dob_datetime = datetime.strptime(dob_str, "%d-%m-%Y")
curr_datetime = datetime.today()

print(type(dob_datetime))
print(type(curr_datetime))

period_timedelta = curr_datetime - dob_datetime  # returns difference in 'timedelta'

print(type(period_timedelta))

print(period_timedelta.days // 365)
