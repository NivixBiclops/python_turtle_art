import turtle
t = turtle.Turtle()
t.home()
t.speed("fastest")
for x in range(35):
    t.circle(50)
    t.forward(100)
    t.circle(50)
    t.backward(100)
    t.left(10)
