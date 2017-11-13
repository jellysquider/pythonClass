month = eval(input("Enter the number of the month: "))
year = eval(input("Enter the year: "))
leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if (month <= 12):
    if (month == 1):
        print("January", year, "has 31 days")
    elif (month == 2):
        if (leap_year):
            print("February", year, "has 29 days")
        else:
            print("February", year, "has 28 days")
    elif (month == 3):
        print("March", year, "has 31 days")
    elif (month == 4):
        print("April", year, "has 30 days")
    elif (month == 5):
        print("May", year, "has 31 days")
    elif (month == 6):
        print("June", year, "has 30 days")
    elif (month == 7):
        print("July", year, "has 31 days")
    elif (month == 8):
        print("August", year, "has 31 days")
    elif (month == 9):
        print("September", year, "has 30 days")
    elif (month == 10):
        print("October", year, "has 31 days")
    elif (month == 11):
        print("November", year, "has 30 days")
    elif (month == 12):
        print("December", year, "has 31 days")
else:
    print("You entered the wrong number. Rerun the program.")

#a year is a leap year if it's divisible by 4: 2012, 1992, etc.
#Gets cancelled every 100 years
