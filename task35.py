#35
day = input("Enter a day of the week: ")
if day == "Monday " or "Tuesday" or "Wednesday" or "Thursday":
    print("Weekday")
elif day == "Friday":
    print("TGIF")
else:
    print("WEEKEND")