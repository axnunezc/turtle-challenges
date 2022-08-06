from turtle import Turtle, Screen
import random
import turtle

race_end = True
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-150, -90, -30, 30, 90, 150]
turtle_list = []

for index in range(len(colors)):
    tim = Turtle("turtle")
    tim.color(colors[index])
    tim.penup()
    tim.goto(-230, y_positions[index])
    turtle_list.append(tim)

if user_bet:
    race_end = False

while not race_end:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            race_end = True
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")
        move = random.randint(0, 10)
        turtle.forward(move)

screen.exitonclick()