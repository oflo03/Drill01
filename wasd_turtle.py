import turtle

def move_w():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)

def move_a():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)

def move_s():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)

def move_d():
    turtle.stamp()
    turtle.setheading(360)
    turtle.forward(50)


turtle.shape('turtle')

turtle.onkey(move_w, 'w')
turtle.onkey(move_a, 'a')
turtle.onkey(move_s, 's')
turtle.onkey(move_d, 'd')
turtle.listen()