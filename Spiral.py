import turtle, random
turtle.colormode(255)
t = turtle.Turtle()
t.home()
randint = random.randint
var1 = 0
t.speed("fastest")
for x in range (50):
	r = randint(0,255)
	r = randint(0,255)
	r = randint(0,255)
	turtle.color(r, g, b)
	var1 = var1 + 10
	t.circle(var1,180)
	t.width(var1/20)

    
