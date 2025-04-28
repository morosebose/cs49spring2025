"""
archway.py

Get Karel over an archway

Programmer: Surajit A. Bose, Date: April 25, 2025
"""

from karel.stanfordkarel import *

def main():
    """
    Move Karel from one corner of the world to the other over an archway
    
    Preconditions: 
    - Karel is on the bottom row leftmost corner facing east
    - There is an archway three squares high blocking Karel's way forward
    
    Postconditions:
    - Karel is on the bottom row rightmost corner facing east 
    - Archway is behind Karel
    """
    turn_left()
    move_forward_three()
    turn_right()
    move_forward_three()
    turn_right()
    move_forward_three()
    turn_left()

    
def turn_right():
    """Turn Karel to face right"""
    turn_left()
    turn_left()
    turn_left()
    

def move_forward_three():
    """Move Karel forward three squares at once"""
    move()
    move()
    move()
    
    
if __name__ == "__main__":
    main()