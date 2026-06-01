'''
Hailey Laber
This program creates an enhanced colorful outdoor scene with a house, multiple trees, sun, clouds, flowers, and a path
using Python Turtle graphics and user-defined functions. After refactoring the code into modular functions for basic shapes
and composite figures, the scene was made more populated by easily adding multiple instances of trees, clouds, and flowers,
demonstrating how refactored code enables easier creation of complex compositions. Specific improvements include adding
windows to the house, a winding path, a flower garden, and additional trees and clouds to create a richer, more detailed landscape.
'''

# Import turtle module to draw graphics on the screen
import turtle

# Import math module (used for drawing curves with sine calculations)
import math



# CONSTANTS SECTION
# These variables store positions, sizes, and colors so that
# the code is easy to change and avoids hard-coding values.

# Sun settings (position, size, and color)
SUN_X = 200
SUN_Y = 210
SUN_RADIUS = 50
SUN_COLOR = "yellow"

# Grass (ground) settings
GRASS_X = -400
GRASS_Y = -200
GRASS_WIDTH = 800
GRASS_HEIGHT = 200
GRASS_COLOR = "green"

# House base and roof settings
HOUSE_X = -100
HOUSE_Y = -100
HOUSE_WIDTH = 200
HOUSE_HEIGHT = 150
HOUSE_COLOR = "brown"
ROOF_SIZE = 200
ROOF_COLOR = "red"

# Door settings
DOOR_X = -20
DOOR_Y = -170
DOOR_WIDTH = 40
DOOR_HEIGHT = 80
DOOR_COLOR = "black"

# Tree settings (trunk and leaves)
TREE_WIDTH = 30
TREE_HEIGHT = 100
TREE_COLOR = "saddlebrown"
TREE_LEAVES_RADIUS = 50
TREE_LEAVES_COLOR = "darkgreen"

# Tree positions (used to place multiple trees across the scene)
TREE1_X = -250
TREE1_Y = -100
TREE2_X = 250
TREE2_Y = -100

# Cloud settings (multiple circles combined)
CLOUD_X = -200
CLOUD_Y = 150
CLOUD_RADIUS = 30
CLOUD_COLOR = "white"
CLOUD_OFFSET = 40  # distance between cloud circles

# Window settings
WINDOW_WIDTH = 30
WINDOW_HEIGHT = 30
WINDOW_COLOR = "lightblue"

# Flower settings (stem, petals, and center)
FLOWER_STEM_HEIGHT = 40
FLOWER_STEM_COLOR = "green"
FLOWER_PETAL_RADIUS = 10
FLOWER_PETAL_COLOR = "yellow"
FLOWER_CENTER_RADIUS = 5
FLOWER_CENTER_COLOR = "orange"

# Path settings
PATH_X = -50
PATH_Y = -250
PATH_WIDTH = 100
PATH_HEIGHT = 100
PATH_COLOR = "gray"



# SETUP FUNCTION
# This function creates the turtle and screen and prepares
# everything for drawing.

def setup_turtle():
    """Initialize turtle object and screen settings"""
    t = turtle.Turtle()        # Create a turtle object
    t.speed(0)                # Set speed to fastest (instant drawing)
    screen = turtle.Screen()  # Create the drawing window
    screen.title("Turtle Graphics Assignment")  # Set window title
    return t, screen          # Return both turtle and screen


# BASIC SHAPE FUNCTIONS
# These functions draw simple reusable shapes that are used
# to build more complex objects like houses and trees.

def draw_rectangle(t, width, height, fill_color=None):
    """Draw a rectangle using width and height"""
    if fill_color:
        t.fillcolor(fill_color)  # Set fill color
        t.begin_fill()           # Start filling shape

    # Draw rectangle (2 pairs of sides)
    for _ in range(2):
        t.forward(width)   # Draw width
        t.right(90)
        t.forward(height)  # Draw height
        t.right(90)

    if fill_color:
        t.end_fill()  # Finish filling


def draw_square(t, size, fill_color=None):
    """Draw a square (all sides equal)"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()

    # Loop 4 times for 4 equal sides
    for _ in range(4):
        t.forward(size)
        t.right(90)

    if fill_color:
        t.end_fill()


def draw_triangle(t, size, fill_color=None):
    """Draw an equilateral triangle (used for roof)"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()

    # 3 equal sides, each 120 degrees apart
    for _ in range(3):
        t.forward(size)
        t.left(120)

    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    """Draw a circle (used for sun, clouds, leaves, etc.)"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()

    t.circle(radius)  # Draw circle

    if fill_color:
        t.end_fill()


def draw_polygon(t, sides, size, fill_color=None):
    """Draw a regular polygon with a given number of sides"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()

    angle = 360 / sides  # Calculate turning angle

    # Draw each side
    for _ in range(sides):
        t.forward(size)
        t.right(angle)

    if fill_color:
        t.end_fill()


def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    """Draw a smooth curve using small line segments"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()

    segment_length = length / segments
    original_heading = t.heading()  # Save direction

    # Create curve using sine wave for smooth bending
    for i in range(segments):
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)

    t.setheading(original_heading)  # Reset direction

    if fill_color:
        t.end_fill()


def jump_to(t, x, y):
    """Move turtle without drawing (used for positioning shapes)"""
    t.penup()
    t.goto(x, y)
    t.pendown()


# COMPOSITE OBJECT FUNCTIONS
# These use basic shapes to create more complex objects
# like houses, trees, flowers, etc.

def draw_sun(t):
    """Draw the sun in the sky"""
    jump_to(t, SUN_X, SUN_Y)
    draw_circle(t, SUN_RADIUS, SUN_COLOR)


def draw_grass(t):
    """Draw the green ground at the bottom"""
    jump_to(t, GRASS_X, GRASS_Y)
    draw_rectangle(t, GRASS_WIDTH, GRASS_HEIGHT, GRASS_COLOR)


def draw_house(t):
    """Draw house with base, roof, door, and windows"""

    # Draw main house base
    jump_to(t, HOUSE_X, HOUSE_Y)
    draw_rectangle(t, HOUSE_WIDTH, HOUSE_HEIGHT, HOUSE_COLOR)

    # Draw triangular roof
    jump_to(t, HOUSE_X, HOUSE_Y)
    draw_triangle(t, ROOF_SIZE, ROOF_COLOR)

    # Draw door centered on house
    jump_to(t, DOOR_X, DOOR_Y)
    draw_rectangle(t, DOOR_WIDTH, DOOR_HEIGHT, DOOR_COLOR)

    # Draw windows on left and right side
    jump_to(t, HOUSE_X + 20, HOUSE_Y - 40)
    draw_square(t, WINDOW_WIDTH, WINDOW_COLOR)

    jump_to(t, HOUSE_X + HOUSE_WIDTH - WINDOW_WIDTH - 20, HOUSE_Y - 40)
    draw_square(t, WINDOW_WIDTH, WINDOW_COLOR)


def draw_tree(t, x, y):
    """Draw a tree consisting of trunk and leafy top"""

    # Draw trunk
    jump_to(t, x, y)
    draw_rectangle(t, TREE_WIDTH, TREE_HEIGHT, TREE_COLOR)

    # Draw leaves (circle on top of trunk)
    jump_to(t, x + TREE_WIDTH / 2, y)
    draw_circle(t, TREE_LEAVES_RADIUS, TREE_LEAVES_COLOR)


def draw_cloud(t, x, y):
    """Draw a cloud using three overlapping circles"""

    # First cloud circle
    jump_to(t, x, y)
    draw_circle(t, CLOUD_RADIUS, CLOUD_COLOR)

    # Second cloud circle
    jump_to(t, x + CLOUD_OFFSET, y)
    draw_circle(t, CLOUD_RADIUS, CLOUD_COLOR)

    # Third cloud circle
    jump_to(t, x + 2 * CLOUD_OFFSET, y)
    draw_circle(t, CLOUD_RADIUS, CLOUD_COLOR)


def draw_window(t, x, y):
    """Reusable window function (extra modularity)"""
    jump_to(t, x, y)
    draw_square(t, WINDOW_WIDTH, WINDOW_COLOR)


def draw_flower(t, x, y):
    """Draw a flower with stem, petals, and center"""

    # Draw stem (thin rectangle)
    jump_to(t, x, y)
    t.fillcolor(FLOWER_STEM_COLOR)
    t.begin_fill()
    t.forward(2.5)
    t.left(90)
    t.forward(FLOWER_STEM_HEIGHT)
    t.right(90)
    t.forward(2.5)
    t.right(90)
    t.forward(FLOWER_STEM_HEIGHT)
    t.left(90)
    t.end_fill()

    # Draw petals in a circular pattern
    jump_to(t, x + 2.5, y + FLOWER_STEM_HEIGHT)
    for _ in range(5):
        draw_circle(t, FLOWER_PETAL_RADIUS, FLOWER_PETAL_COLOR)
        t.right(72)  # 360 / 5 petals

    # Draw flower center
    jump_to(t, x + 2.5, y + FLOWER_STEM_HEIGHT)
    draw_circle(t, FLOWER_CENTER_RADIUS, FLOWER_CENTER_COLOR)


def draw_path(t):
    """Draw the path leading to the house"""
    jump_to(t, PATH_X, PATH_Y)
    draw_rectangle(t, PATH_WIDTH, PATH_HEIGHT, PATH_COLOR)


# MAIN SCENE FUNCTION
# This function calls all other functions to build the full scene

def draw_scene(t):
    """Draw complete outdoor scene"""

    # Set sky background color
    screen = t.getscreen()
    screen.bgcolor("skyblue")

    # Draw main elements
    draw_sun(t)
    draw_grass(t)
    draw_house(t)

    # Draw multiple trees for a more detailed scene
    draw_tree(t, TREE1_X, TREE1_Y)
    draw_tree(t, TREE2_X, TREE2_Y)
    draw_tree(t, TREE1_X - 100, TREE1_Y)
    draw_tree(t, TREE2_X + 100, TREE2_Y)
    draw_tree(t, TREE1_X - 50, TREE1_Y)

    # Draw multiple clouds across the sky
    draw_cloud(t, CLOUD_X, CLOUD_Y)
    draw_cloud(t, CLOUD_X + 200, CLOUD_Y - 20)
    draw_cloud(t, CLOUD_X + 400, CLOUD_Y + 30)
    draw_cloud(t, CLOUD_X - 100, CLOUD_Y + 50)

    # Draw flowers on left side
    for i in range(4):
        draw_flower(t, GRASS_X + 100 + i * 50, GRASS_Y)

    # Draw flowers on right side (mirrored placement)
    for i in range(4):
        draw_flower(t, -GRASS_X - 100 - i * 50, GRASS_Y)

    # Draw path leading to house
    draw_path(t)


# MAIN FUNCTION
# This starts the program and runs everything

def main():
    """Main function to run the program"""
    t, screen = setup_turtle()  # Set up turtle and screen
    draw_scene(t)               # Draw entire scene
    screen.mainloop()           # Keep window open


# Run the program only if file is executed directly
if __name__ == "__main__":
    main()