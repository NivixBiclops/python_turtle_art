import turtle, random
t = turtle.Turtle()
t.speed("fastest")
t.home()
randint = random.randint
var1 = 0
turtle.colormode(255)
for x in range (70):
	r = randint(0, 255)
	g = randint(0, 255)
	b = randint(0, 255)
	t.color(r, g, b)
	t.circle(60)
	t.forward(170)
	t.backward(170)
	t.setheading(var1)
	var1 = var1 + 5