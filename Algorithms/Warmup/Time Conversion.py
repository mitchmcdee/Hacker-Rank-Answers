time = input().strip()
hours, mins, seconds = time.split(":")
dayHalf = seconds[-2:]

hours, mins, seconds = int(hours), int(mins), int(seconds[:-2])

if dayHalf == "PM" and hours != 12:
    hours += 12
elif dayHalf == "AM" and hours == 12:
    hours = 0
    
print("{0:02d}:{1:02d}:{2:02d}".format(hours, mins, seconds))