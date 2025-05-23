"""
various_fors.py

Demonstrate the different ranges in for loops.

Programmer: Surajit A. Bose, Date: May 23, 2025
"""

def main():
    # print Hello, World three times
    # loop starts with i at 0 and continues until i is 3
    # loop does not execute when i reaches 5
    for i in range(3):              # implicitly this is range(0, 3, 1)
        print("Hello, World")
    print()
    
    # print the first 10 even numbers
    for i in range(10):
        print(i * 2)                # Use the 'i' value inside the for-loop
    print()
    
    # print the first 10 odd numbers
    # loop does not execute once i reaches or goes beyond 20
    for i in range (1, 20, 2):      # specify start, stop, step
        print(i)
    print()
    
    # print with a decreasing value of i
    # i starts at 5, decreases by 1 until it reaches 1
    # loop does not run when i is 1
    for i in range(5, 1, -1):
        print(f"I have {i} marbles left")
    print("I'm down to my last marble!")
    
    print()
   
if __name__ == "__main__":
    main()