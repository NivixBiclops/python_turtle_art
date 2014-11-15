import turtle, random
colors = ["red","orange","yellow","green","blue","purple","yellow"]
turtle.setup(500,500,0,0)
turtle.bgcolor("black")
t = turtle.Turtle()
t.home()
t.color("white")
for x in range(100):
    mycolor = random.randint(0,6)
    xpos = random.randint(-250,250)
    ypos = random.randint(-250,250)
    t.goto(xpos,ypos)
    t.dot(20,colors[mycolor])
t.invisible()
