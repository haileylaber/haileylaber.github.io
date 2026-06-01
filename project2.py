'''
Hailey Laber
This program creates a colorful outdoor scene with a house, trees, sun, and clouds
using Python Turtle graphics and user-defined functions.

'''


# loads the Turtle graphics module, which is a built-in library in Python
import turtle
import math

def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen


def draw_rectangle(t, width, height, fill_color=None):
    """Draw a rectangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_square(t, size, fill_color=None):
    """Draw a square with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_triangle(t, size, fill_color=None):
    """Draw an equilateral triangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    """Draw a circle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()


def draw_polygon(t, sides, size, fill_color=None):
    """Draw a regular polygon with given number of sides"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()

def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    """
    Draw a curved line using small line segments
    
    Parameters:
    - t: turtle object
    - length: total length of the curve
    - curve_factor: positive for upward curve, negative for downward curve
    - segments: number of segments (higher = smoother curve)
    - fill_color: optional color to fill if creating a closed shape
    """
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
        
    segment_length = length / segments
    # Save the original heading
    original_heading = t.heading()
    
    for i in range(segments):
        # Calculate the angle for this segment
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)  # Reset the angle for the next segment
    
    # Reset to original heading
    t.setheading(original_heading)
    
    if fill_color:
        t.end_fill()
        
def jump_to(t, x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()


#YOU MUST add function calls in this draw_scence function defintion
# to create your scence (No statements outside of function definiions)
def draw_scene(t):
    """Draw a colorful scene with various shapes"""
    # Set background color
    screen = t.getscreen()
    screen.bgcolor("skyblue")

    # sun
    jump_to(t, 200, 210) #move to top right corner
    draw_circle(t, 50, "yellow")#draws circle for the sun and set the color to yellow

    # Grass (rectangle at bottom)
    jump_to(t, -400, -200)#move to bottom left corner
    draw_rectangle(t, 800, 200, "green")#draw grass across the bottom of the screen and set the color to green

    #  House base
    jump_to(t, -100, -100)#move to center of the screen
    draw_rectangle(t, 200, 150, "brown")#draw the base of the house and set color to brown

    # Roof above the house base
    jump_to(t, -100, -100)#move to the top left corner of the house base
    draw_triangle(t, 200, "red")# draws triangle for the roof of the house and set color to red

    # Door
    jump_to(t, -20, -170)# move to center of the house base and draw triangle for the door of the house
    draw_rectangle(t, 40, 80, "black")#draws rectangle for the door and sets the color to black

    # Tree 1 (trunk)
    jump_to(t, -250, -100)#move to the left of the house 
    draw_rectangle(t, 30, 100, "saddlebrown")#draws rectangle for the trunk of the tree and set color to saddle brown

    # Tree 1 leaves
    jump_to(t, -235, -100)# move to the top center of the trunk of the tree 
    draw_circle(t, 50, "darkgreen")#draws circle for the leaves of the tree and sets the color to darkgreen

    # Tree 2(trunk)
    jump_to(t, 250, -100)#move to the right of the house
    draw_rectangle(t, 30, 100, "saddlebrown")

    # Tree 2 leaves
    jump_to(t, 265, -100)
    draw_circle(t, 50, "darkgreen")

    # Cloud
    jump_to(t, -200, 150)# move to the top left corner of the screen
    draw_circle(t, 30, "white")#draws circle for the cloud and sets the color to white

    jump_to(t, -160, 150)# move to the right of the first cloud circle and draw another circle for the cloud
    draw_circle(t, 30, "white")#draws circle for the cloud and sets the color to white

    jump_to(t, -120, 150)# move to the right of the second cloud circle and draw another circle for the cloud
    draw_circle(t, 30, "white")#draws circle for the cloud and sets the color to white
    
    

# This is the main() function that starts off the execution
def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()

# if this script is executed, call the main() function
# meaning when is file is run directly
if __name__ == "__main__":
    main()