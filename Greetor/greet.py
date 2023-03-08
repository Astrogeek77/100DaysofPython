import time
# timestamp = time.strftime('%H:%M:%S %A:%B:%c')

hours = int(time.strftime('%H'))
minutes = int(time.strftime('%M'))
seconds = int(time.strftime('%S'))
day = time.strftime('%A')
month = time.strftime('%B')
dayOfMonth = time.strftime('%d')
weekNumber = time.strftime('%U')
year = time.strftime('%Y')
local_time = time.strftime('%x')
local_date = time.strftime('%X')
gmtdiff = time.strftime('%z')
timezone = time.strftime('%Z')

curr_time = time.strftime('%H:%M:%S %p')
print("-" * 30)
print("Current Time: ", curr_time)
print("-" * 30)
print("Current Date: ", dayOfMonth + ' ' + month + ', ' + day)
print("-" * 30)
print(f'Current is the {weekNumber}th week of the year {year}.')
print("-" * 30)
print(f"Local Time: {local_time}, Local Date: {local_date}, {gmtdiff}, {timezone}")
print("-" * 30)

# https://docs.python.org/3/library/time.html#time.strftime

if (hours > 4 < 12):
    print("\nGood Morning Buddy")
elif (hours > 12 < 18):
    print("\nGood Afternoon Buddy")
elif (hours > 18 < 21):
    print("\nGood Evening Buddy")
elif (hours > 21 < 4):
    print("\nGood Night Buddy")
