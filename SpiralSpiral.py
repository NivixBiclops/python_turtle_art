import turtle, random
t = turtle.Turtle()
randint = random.randint
t.home()
turtle.bgcolor("black")
turtle.colormode(255)
t.speed("fastest")
for x in range(35):
	r = randint(0, 255)
	g = randint(0, 255)
	b = randint(0, 255)
	t.color(r, g, b)
	t.circle(50)
	t.forward(100)
	t.circle(50)
	t.backward(100)
	t.left(10)