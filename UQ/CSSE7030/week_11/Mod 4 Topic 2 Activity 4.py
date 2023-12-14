import turtle

def square():
    turtle.reset()
    turtle.up()
    turtle.goto(-100,-100)
    turtle.down()
    turtle.begin_fill()
    turtle.color('red')
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.end_fill()
