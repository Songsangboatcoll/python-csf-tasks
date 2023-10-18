#37 only spring coming
try:
    month = input("Enter a month: ")
    print(month)
    if month == "January" or "February" or "March":
        print("Spring")
    elif month == "April" or "May" or "June":
        print("Summer")
    elif month == "July" or "August" or "September":
        print("Autumn")
    else:
        print("Winter")
except:
    print("Invalid month")
finally:
    print("The season of your month is found out")
