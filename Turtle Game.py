# Maze Game 
# Made by Abhi239 (I like this shortform)
# Spent way to much time on it 
# Enjoy :) 


# Make sure to import the turtle library to actually be able to make the game
import turtle 

# This will come in handy when it comes to write things 
gameFont = ("Times New Roman", 20, 'italic')

# Just the basic steps needed before the major coding starts
wn = turtle.Screen()
wn.setup(width=800, height=500)
wn.bgcolor('black')
wn.title("Maze Game")

# abhi player turtle
abhi = turtle.Turtle()
abhi.color('blue', 'red') 
abhi.shape('classic')
abhi.shapesize(3, 3, 1)

# P2 player turtle 
P2 = turtle.Turtle()
P2.color('orange', 'white') 
P2.shape('classic')
P2.shapesize(3, 3, 1)

# l1 draw turtle 
l1 = turtle.Turtle()
l1.shapesize(0.2, 0.2, 0.2)
l1.shape('square')
l1.color('white', 'white')
l1.pensize(5)
l1.goto(0,0)

#l2 draw turtle 
l2 = turtle.Turtle()
l2.shapesize(0.2, 0.2, 0.2)
l2.shape('square')
l2.color('green', 'green')
l2.pensize(5)
l2.pu()
l2.goto(720,415)
l2.pd()

# Gives you a message in the beginning to play in full screen to get the entire benefits and how to sprint
l1.write("Play in Full Screen", align="center", font=gameFont)
l1.pu()
l1.goto(0, -100)
l1.pd()
l1.write("P1/abhi turtle is red. Player 1 can sprint with holding down the 'v' key", align="center", font=gameFont)
l1.pu()
l1.goto(0, -200)
l1.pd()
l1.write("P2 is white. Player 2 can sprint with holding down the 'm' key", align="center", font=gameFont)

# When you click on Abhi turtle, it will spin in place 
def spin(x,y):
    abhi.lt(360)
abhi.onclick(spin)

# When you click on P2 turtle, it will spin in place
def spin(v,c):
    P2.lt(360)
P2.onclick(spin)

# Very useful function to make a line for the maze. Will be used a lot
def makeLine(x, y, z, a):
    l1.speed(100)
    l1.pu()
    l1.goto(x, y)
    l1.pd()
    l1.setheading(z)
    l1.fd(a)

# Function definition for up for abhi
def upOne():
    abhi.setheading(90)
    abhi.fd(50)

# Function definition for down for abhi
def downOne():
    abhi.setheading(270)
    abhi.fd(50)

# Function definition for left for abhi
def leftOne():
    abhi.setheading(180)
    abhi.fd(50)

# Function definition for right for abhi
def rightOne():
    abhi.setheading(0)
    abhi.fd(50)

# Function definition for up for P2
def upTwo():
    P2.setheading(90)
    P2.fd(50)

# Function definition for down for P2
def downTwo():
    P2.setheading(270)
    P2.fd(50)

# Function definition for left for P2
def leftTwo():
    P2.setheading(180)
    P2.fd(50)

# Function definition for right for P2
def rightTwo():
    P2.setheading(0)
    P2.fd(50)

# Sprint feature for abhi
def sprintOne():
    abhi.speed(50)

# Normal speed for abhi
def normalSpeedOne():
    abhi.speed(5)

# Sprint feature for P2
def sprintTwo():
    P2.speed(50)

# Normal speed for P2
def normalSpeedTwo():
    P2.speed(5)

# Details of where to start for abhi
abhi.speed(1000)
abhi.pu()
abhi.goto(-725, -400)
abhi.pd()
abhi.speed(5)


# Details of where to start for P2
P2.speed(1000)
P2.pu()
P2.goto(-725, -400)
P2.pd()
P2.speed(5)


# The Window listens 
wn.listen()
# When the certain key is pressed it moves accordingly 
wn.onkeypress(upOne, "w") # Assigning a key a certain an input 
wn.onkeypress(downOne, 's')
wn.onkeypress(rightOne, 'd')
wn.onkeypress(leftOne, 'a')
wn.onkeypress(upTwo, "Up")
wn.onkeypress(downTwo, 'Down')
wn.onkeypress(rightTwo, 'Right')
wn.onkeypress(leftTwo, 'Left')
wn.onkeypress(sprintOne, 'v')
wn.onkeyrelease(normalSpeedOne, 'v')
wn.onkeypress(sprintTwo, 'm')
wn.onkeyrelease(normalSpeedTwo, 'm')

# This give you some time to read the text and act accordingly 
o = 60000
while o > 0:
    print(o)
    o -= 1 # Keeps subtracting from o until it reaches 0 
    if o <= 0: 
        l1.clear() # When it reaches 0, it will clear all the writing and start making the maze 

#The calling of the functions to make an accurate straight line 
makeLine(-700, -415, 90, 750)
makeLine(-762, -415, 90, 870)
makeLine(-775, 415, 0, 1550)
makeLine(-400, 300, 270, 715)
makeLine(-200, 415, 270, 350)
makeLine(100, 300, 0, 300)
makeLine(-400, 275, 0, 145)
makeLine(756, -415, 90, 787)
makeLine(-775, -410, 0, 1550)
makeLine(100, 150, 0, 400)
makeLine(100, 415, 270, 400)
makeLine(300, -415, 90, 450)
makeLine(200, -300, 90, 400)
makeLine(100, -115, 180, 500)
makeLine(0, 350, 270, 600)
makeLine(-400, 0, 0, 180)
makeLine(-100, 415, 270, 480)
makeLine(-550, 380, 270, 700)
makeLine(-650, 230, 0, 200)
makeLine(-400, -300, 0, 450)
makeLine(-200, -200, 270, 150)
makeLine(-200, 150, 180, 150)
makeLine(600, 315, 270, 500)
makeLine(760, 0, 180, 100)
makeLine(600, 150, 0, 100)
makeLine(600, 250, 180, 300)
makeLine(450, 150, 270, 500)
makeLine(450, -275, 0, 225)

# Makes the green box that directs you where the end is
l2.setheading(0)
l2.fd(36)
l2.setheading(270)
l2.fd(40)
l2.setheading(180)
l2.fd(36)
l2.setheading(90)
l2.fd(40)
l2.hideturtle()

# Function definition of when abhi turtle falls off
def fellOffAbhi():
    abhi.goto(0,0)
    l1.goto(0, 100)
    l1.clear()
    l2.clear()
    abhi.clear()
    l1.write("Player One Fell Off The Edge... Game Over", align="center", font=gameFont)
    l1.hideturtle()
    turtle.done()
    

#Function definition of when P2 turtle falls off 
def fellOffP2():
    P2.goto(0,0)
    l1.goto(0, 100)
    l1.clear()
    l2.clear()
    P2.clear()
    l1.write("Player Two Fell Off The Edge... Game Over", align="center", font=gameFont)
    l1.hideturtle()
    turtle.done()

# Function definition of when Abhi runs into a wall
def ranIntoWallAbhi():
    abhi.goto(0,0)
    l1.goto(0, 100)
    l1.clear()
    l2.clear()
    abhi.clear()
    l1.write("Player 1 Ran Into A Wall...")
    l1.hideturtle()
    turtle.done()

# Function definition of when P2 runs into a wall
def ranIntoWallP2():
    P2.goto(0,0)
    l1.goto(0,100)
    l1.clear()
    l2.clear()
    P2.clear()
    l1.write("Player 2 Ran Into A Wall...")
    l1.hideturtle()
    turtle.done()

# Function definition of when abhi turtle completes the maze 
def completeAbhi():
    abhi.goto(0,0)
    l1.goto(0, 100)
    l1.clear()
    l2.clear()
    abhi.clear()
    l1.write("Player One completed the maze first and wins", align="center", font=gameFont)
    l1.hideturtle()
    turtle.done()

# Function definition of when P2 turtle completes the maze 
def completeP2():
    P2.goto(0,0)
    l1.goto(0, 100)
    l1.clear()
    l2.clear()
    P2.clear()
    l1.write("PLayer 2 has completed the maze first and wins", align="center", font=gameFont)
    l1.hideturtle()
    turtle.done()    

# While true loop that keeps everything running and keeps tags on the position of the turtle players 
while True: 
    x,y=abhi.pos()
    v,c=P2.pos()
    if x < -762 or x > 755 or y > 415 or y < -410:
        fellOffAbhi()
        break
    if v < -762 or v > 755 or c > 415 or c < -410:
        fellOffP2()
        break
    if v > 720 and 415>c>375:
        completeP2()
        break
    if x > 720 and 415>y>375:
        completeAbhi()
        break
    wn.update()