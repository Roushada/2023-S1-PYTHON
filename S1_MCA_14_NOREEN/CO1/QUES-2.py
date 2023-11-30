current_year=2023
final_year=int(input("Enter The Final Year:"))
leap_year=[year for year in range(current_year,final_year)
           if(year%4==0)]
print("Leap Years From",current_year,"To",final_year,"Are:",leap_year)
