import turtle, random
t = turtle.Turtle()
ran = random.randint
turtle.colormode(255)
t.home()
turtle.bgcolor("black")
t.speed("fastest")
for x in range (0, 180):
    r = ran(0, 255)
    g = ran(0, 255)
    b = ran(0, 255)
    t.color(r, g, b)
    length = ran(10,350)
    t.forward(length)
    t.backward(length)
    t.left(2)
