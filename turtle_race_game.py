from turtle import Turtle,Screen
import random

canvas = Screen()
canvas.setup(width=500,height=400)
userBet = canvas.textinput(title="Make your bet",prompt="Which turtle will win this race ? Enter your color: ").lower()


colors = ["red","orange","yellow","green","blue","purple"]
positions = [-70,-40,-10,20,50,80]
turtles = []

isAlive = True
for i in range(len(colors)):
    brush = Turtle(shape="turtle")
    brush.color(colors[i])
    brush.penup()
    brush.goto(x=-230,y= positions[i])
    turtles.append(brush)


while isAlive:
    for i in range(len(colors)):
        turtles[i].forward(random.randrange(0,10))
        if turtles[i].xcor() > 230:
            if turtles[i].color()[0] == userBet:
                print(f"sucsess {turtles[i].color()[0]} turtle is win")
            else:
                print(f"unsuccessful {turtles[i].color()[0]} turtle is win")
            isAlive = False        


canvas.exitonclick()