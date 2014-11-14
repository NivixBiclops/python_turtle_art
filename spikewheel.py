import turtle
t = turtle.Turtle()
t.speed("fastest")
var1 = 0
for x in range (110):
    t.circle(60)
    t.forward(170)
    t.backward(170)
    t.setheading(var1)
    var1 = var1 + 5