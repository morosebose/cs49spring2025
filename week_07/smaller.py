"""
smaller.py

Demonstrate functions, function calls, parameters/arguments, and return values

Programmer: Surajit A. Bose, Date: May 22, 2025
"""

def main():
    """Ask user to input two numbers. Print out the smaller number."""
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))

    # Function call. Caller: main(), called function: smaller(),
    # arguments: first_num, second_num
    smaller_num = smaller(first_num, second_num)
    print(f"The smaller number is {smaller_num}.")
    print()

# function parameters: num1, num2
def smaller(num1, num2):
    """Return smaller of two integers. If two are equal, return second integer."""
    if num1 < num2:
        return num1     # Return statement. Return value: num1
    return num2         # Return statement. Return value: num2

    # Can do this as a one-liner:
    # return num1 if num1 < num2 else num2

if __name__ == "__main__":
    main()
    