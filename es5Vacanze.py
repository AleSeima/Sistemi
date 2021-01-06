import turtle
DIM_CAMPO = 175

robot = turtle.Turtle()
robot.penup()
robot.goto(0,0)
bordo = turtle.Turtle() 
bordo.speed(10)

win = turtle.Screen()

def disegnaBordo():
    bordo.penup()
    bordo.goto(-1 * DIM_CAMPO,-1 * DIM_CAMPO)
    bordo.pendown()

    for k in range (4):
        bordo.forward(350)
        bordo.left(90)

def up():
    coordinate = robot.position()
    
    if(coordinate[0] < DIM_CAMPO and coordinate[0] > -1 * DIM_CAMPO and coordinate[1] < DIM_CAMPO and coordinate[1] > -1 * DIM_CAMPO):
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