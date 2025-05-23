"""
bonus_belgium_match_case.py

Demonstrate use of match case in Python using 1969 song lyric:
    If it's Tuesday, this must be Belgium
    If it's Wednesday, this must be Rome
    If it's Thursday, this must be Montreux
    I feel I never wanna go home.
    
Note: This requires Python 3.10 or above and will not work in Code in Place IDE.

Programmer: Surajit A. Bose, Date: May 22, 2025
"""

def main():
    """Ask user to enter a day of the week and print out corresponding line from song"""
    day = input("Enter day of the week: ").title()
    
    match day:
        case "Tuesday":
            place = "Belgium"
        case "Wednesday":
            place = "Rome"
        case "Thursday":
            place = "Montreux"
        case _:
            place = None

    match place:
        case None:
            print("I feel I never wanna go home")
        case _:
            print (f"If it's {day} this must be {place}")
            
    print()
    
if __name__ == "__main__":
    main()

