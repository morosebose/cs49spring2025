"""
Program requirements:
- Ask the user to input a year
- Determine whether that year is a leap year
- Print out the result

Three chained tests are involved:
- Is the year exactly divisible by four?
- If so, is it exactly divisible by 100?
- If so, is it exactly divisible by 400?

Hint: 
- How do we know whether a given number is exactly divisible by another given number? 
- What Python operator can we use for this?

Test cases: 
- Leap years 1984, 2020, 1600
- Non-leap years 2025, 1700
"""

def main():
    year = int(input("Enter a year: "))

    # your code here
    
    # blank line for uncrowded screen output
    print()

if __name__ == "__main__":
    main()