"""
check_leap_year_2.py

Ask user to input a year, then print whether or not that is a leap year.

This approach uses guard conditions to filter out non-leap years and concludes
that a year is a leap year only if the year gets past all the guard conditions.

This results in less nested, easier to follow code.

Programmer: Surajit A. Bose; Date: May 21, 2025
"""

def main():
    year = int(input("Enter a year: "))

    # all leap years should be evenly divisible by 4
    if year % 4 != 0:
        is_leap = False

    # century years should also be evenly divisible by 400
    elif year % 100 == 0 and year % 400 != 0:
        is_leap = False

    # all tests passed
    else:
        is_leap = True
    
    # print out result
    if is_leap:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
    
    # blank line for uncrowded screen output
    print()

if __name__ == "__main__":
    main()