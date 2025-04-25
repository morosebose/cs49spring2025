"""
main.py

Karel moves a beeper from the bottom row to the top row

Programmer: Surajit A Bose, Date: January 6, 2025
"""

from karel.stanfordkarel import *

def main():
    """
    Move Karel and beeper to top row
    
    Preconditions:
    - Karel is in the bottom left corner, facing east
    - There is a beeper immediately in front of Karel

    Postconditions:
    - Karel is in the top right corner, facing east
    - Beeper has been moved and is immediately behind Karel
    """
    move()
    pick_beeper()
    turn_left()
    move()
    move()
    turn_left()
    turn_left()
    turn_left()
    put_beeper()
    move()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()