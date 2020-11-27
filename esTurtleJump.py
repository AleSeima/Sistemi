import turtle

robot = turtle.Turtle()
win = turtle.Screen()

def up():
    robot.forward(50)

def down():
    robot.backward(50)

def left():
    robot.left(90)
    robot.forward(50)

def right():
    robot.right(90)
    robot.forward(50)

win.title("My game")
win.bgcolor("green")
win.setup(width=800, height=800)

win.listen() #mette la finestra in ascolto di eventi (es: pressione tasti)
win.onkey(up, "Up")
win.onkey(down, "Down")
win.onkey(left, "Left")
win.onkey(right, "Right")


win.mainloop()