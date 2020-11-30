import turtle

robot = turtle.Turtle()
robot.penup()
robot.goto(0,0)
bordo = turtle.Turtle() 
bordo.speed(10)

win = turtle.Screen()

def disegnaBordo():
    bordo.penup()
    bordo.goto(-175,-175)
    bordo.pendown()

    for k in range (4):
        bordo.forward(350)
        bordo.left(90)

def up():
    coordinate = robot.position()
    
    if(coordinate[0] < 175 and coordinate[0] > -175 and coordinate[1] < 175 and coordinate[1] > -175):
        robot.forward(25)
    else:
        robot.goto(0,0)

def left():
    robot.left(90)
    robot.forward(50)

def right():
    robot.right(90)
    robot.forward(50)

disegnaBordo()
win.title("My game")
win.bgcolor("green")
win.setup(width=800, height=800)

win.listen() #mette la finestra in ascolto di eventi (es: pressione tasti)
win.onkey(up, "Up")
win.onkey(left, "Left")
win.onkey(right, "Right")


win.mainloop()