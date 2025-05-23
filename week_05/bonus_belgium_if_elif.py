"""
bonus_belgium_if_elif.py

Demonstrate use of if-elif-else in Python using 1969 song lyric:
    If it's Tuesday, this must be Belgium
    If it's Wednesday, this must be Rome
    If it's Thursday, this must be Montreux
    I feel I never wanna go home.
    
Use falsiness of None to make code more Pythonic

Programmer: Surajit A. Bose, Date: May 22, 2025
"""

def main():
    """Ask user to enter a day of the week and print out corresponding line from song"""
    day = input("Enter day of the week: ").title()

    if day == "Tuesday":
        place = "Belgium"
    elif day == "Wednesday":
        place = "Rome"
    elif day == "Thursday":
        place = "Montreux"
    else:
        place = None

    if place:
        print (f"If it's {day} this must be {place}")
    else:
        print("I feel I never wanna go home")

    print()
    
if __name__ == "__main__":
    main()

