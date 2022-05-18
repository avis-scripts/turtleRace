import random
import time
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.tracer(0)
screen.title("Fast and Furious Turtle Edition")
screen.bgcolor("black")
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "white", "pink"]
y_positions = [- 100, -70, -40, -10, 20, 50, 80, 110]
all_turtles = []
score_turtle = Turtle()
score_turtle.color("white")
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.goto(0, -150)

for turtle_index in range(len(y_positions)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Place your bet!!",
                            prompt=f"Which turtle will win the race? Enter a colour:\n{colors}")

if user_bet:
    is_race_on = True

while is_race_on:
    screen.update()
    time.sleep(0.1)
    for turtle in all_turtles:
        if turtle.xcor() > 225:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                score_turtle.write(f"You have won! The {winning_color} turtle is the winner!", align="center",
                                   font=("Arial", 15, "normal"))
                score_turtle.goto(0, -185)
                score_turtle.write("GAME OVER", align="center", font=("Arial", 20, "bold"))
            else:
                score_turtle.write(f"You have lost! The {winning_color} turtle is the winner!", align="center",
                                   font=("Arial", 15, "normal"))
                score_turtle.goto(0, -185)
                score_turtle.write("GAME OVER", align="center", font=("Arial", 20, "bold"))
                is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
