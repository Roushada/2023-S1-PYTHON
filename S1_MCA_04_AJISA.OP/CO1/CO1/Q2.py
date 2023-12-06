current_year = int(input("Enter the current year:"))
future_year = int(input("Enter the future year:"))
if (current_year<future_year):
    print("Leap years are")
    for year in range(current_year,future_year+1):
        if(year%4==0 and year%100!=0):
            print(year)
else:
    print("no future Leap years found")
