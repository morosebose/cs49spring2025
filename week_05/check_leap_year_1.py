"""
check_leap_year_1.py

Ask user to input a year, then print whether or not that is a leap year.

This is the beginner's approach. Nested if-else conditions make this hard to understand.

Programmer: Surajit A. Bose; Date: May 21, 2025
"""

def main():
    year = int(input("Enter a year: "))

    if year % 4 == 0:               # all leap years are exactly divisible by 4
        if year % 100 == 0:         # century years should also be divisible by 400
            if year % 400 == 0:
                is_leap = True      # century year exactly divisible by 400, e.g. 2000
            else:
                is_leap = False     # century year not divisible by 400, e.g. 1900
        else: 
            is_leap = True          # non-century year exactly divisible by 4
    else:
        is_leap = False             # any year not exactly divisible by 4
    
    # print out result
    if is_leap:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
    
    # blank line for uncrowded screen output
    print()

if __name__ == "__main__":
    main()