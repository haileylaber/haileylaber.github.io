from turtle import *

# background color
screen = Screen()
screen.bgcolor("CornflowerBlue")

color("green")  # grass color

#variables
tree_height = 300 #sets the height of the tree
sun_size = 60 #sets radius or size of the sun

#pen speed
speed(20)

# grass start out placement
penup()
goto(-380, -345)
pendown()

#number of triangles for grass
for i in range(15):
    begin_fill()
    #triangles
    for j in range(3):
        forward(50)
        left(120)
    end_fill()

    # move to the right for next triangle
    penup()
    forward(50)
    pendown()

# move pen to start sun in top left corner
penup()
goto(-230, 150)
pendown()

#draw circle for sun
color("yellow")
begin_fill()
circle(sun_size)
end_fill()

# go to top edge of sun
penup()
goto(-230, 150 + sun_size)  
setheading(0)

# number of rays in loop to be around the sun
for i in range(12):  
    penup()
    forward(sun_size) #distance = radius
    pendown()
    begin_fill()
    for j in range(3): #draws the triangles to look like rays
        forward(15)
        left(120)
    end_fill()
    penup()
    backward(sun_size)
    right(30) #rotates 30 degrees so next ray will be at a new angle

# moves pen to bottom right corner to start drawing the trees
penup()
goto(180, -345)
pendown()

# trunk
setheading(90) #points the pen straight up at a 90 degree angle
color("chocolate4") #sets color for the trunk of the tree

#draws rectangle for the trunk
begin_fill()
forward(tree_height) #left side upwards
right(90)
forward(60) #tops width
right(90)
forward(tree_height) #right side downwards
right(90)
forward(60) #closes shape
end_fill()

# pen moves to middle of trunk to start the "leaves"
penup()
goto(90, -490 + tree_height)
pendown()

color("darkgreen") #set color for tree

for i in range(3):

    # conditional changes the traingles size
    if i == 0:
        size = 250   # bottom biggest triangle for the base
    elif i == 1:
        size = 180   # middle 
    else:
        size = 120    # top is smallest part of tree 

    penup()
    goto(90 + (i * 30), -490 + tree_height + (i * 100))  # makes pen move upward and back to the center
    pendown()

    begin_fill()
    setheading(0)
    for j in range(3): #triangles
        forward(size)
        left(120)
    end_fill()

#cloud 1 placement
penup()
goto(100, 200)
pendown()
color("white")

#draws 4 circles in different places to make the cloud shape
begin_fill()
circle(30)
end_fill()

penup()
goto(130, 220)
pendown()
begin_fill()
circle(35)
end_fill()

penup()
goto(170, 200)
pendown()
begin_fill()
circle(30)
end_fill()

penup()
goto(135, 180)
pendown()
begin_fill()
circle(25)
end_fill()

# cloud 2 between the sun and trees placement
penup()
goto(-50, 100)
pendown()

color("white")

begin_fill()
circle(30)
end_fill()

penup()
goto(-20, 120)
pendown()
begin_fill()
circle(35)
end_fill()

# cloud 2 between the sun and trees placement
penup()
goto(-50, 100)
pendown()

color("white")

begin_fill()
circle(30)
end_fill()

penup()
goto(-20, 120)
pendown()
begin_fill()
circle(35)
end_fill()

penup()
goto(20, 100)
pendown()
begin_fill()
circle(30)
end_fill()

penup()
goto(-15, 90)
pendown()
begin_fill()
circle(25)
end_fill()

done() #ends code

