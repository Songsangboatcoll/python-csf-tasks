#37 only spring com
month = input("Enter a month: ")
print(month)
if month == "January" or "February" or "March":
    print("Spring")
elif month == "April" or "May" or "June":
    print("Summer")
elif month == "July" or "August" or "September":
    print("Autumn")
elif month == "October" or "November" or "December":
    print("Winter")
else:
    print("Invalid month")
