"""
embiggen_circle.py

Animate a circle growing on the canvas.

Programmer: Surajit A. Bose, Date: 2024.06.07
"""

from graphics import Canvas
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
START_SIZE = 0              # circle starting size
END_SIZE = 200              # circle ending size
CHANGE_RATE = 2             # rate at which animation changes, in pixels
DELAY = 0.02                # pause between successive renderings, in seconds


def embiggen_circle():
    """
    Draw a purple circle growing between specified start and end sizes.
    
    Preconditions: 
        - END_SIZE is greater than START_SIZE
        - END_SIZE will fit within canvas dimensions.
    """
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    size = START_SIZE
    while size <= END_SIZE:
        start_x = CANVAS_WIDTH / 2 - size / 2
        start_y = CANVAS_HEIGHT / 2 - size / 2
        circle = canvas.create_oval(start_x, start_y,
            start_x + size, start_y + size, 'purple')
        size += CHANGE_RATE
        time.sleep(DELAY)       

if __name__ == '__main__':
    embiggen_circle()