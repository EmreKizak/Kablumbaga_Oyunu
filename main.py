import random
import turtle
from datetime import time

drawing = turtle.Screen()
drawing = turtle.bgcolor("light blue")
drawing = turtle.title("kaplumbağa oyunu")
Font = ('Arial',30,'normal')
score = 0
game_over= False
turtle_list = []
top_height = turtle.window_height() / 2
y = top_height * 0.9
x_kor = [-20, -10, 0, 10, 20]
y_kor = [20 , 10 ,0 ,-10, -20]
grid_size = 13
score_turtle =turtle.Turtle()
countdown_turtle = turtle.Turtle()
def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.setpos(0,y)
    score_turtle.color("dark blue")
    score_turtle.write(arg="Score : 0",move=False,align="center",font=Font)
def make_turtle(x ,y):

    t= turtle.Turtle()
    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="Score : {}".format(score), move=False, align="center", font=Font)
    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)
def setup_turtles():
    for x in x_kor:
        for y in y_kor:
            make_turtle(x, y)
def vision_turtle():
    for t in turtle_list:
        t.hideturtle()
def show_turtles():
    if not game_over:
        vision_turtle()
        random.choice(turtle_list).showturtle()
        turtle.ontimer(show_turtles, 500)
def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    top_height = turtle.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.setpos(0, y - 30)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.color("dark blue")
        countdown_turtle.write(arg="Time : {}".format(time), move=False, align="center", font=Font)
        turtle.ontimer(lambda :countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        vision_turtle()
        countdown_turtle.write(arg="Game Over",move=False, align="center",font=Font)
def start_game_up():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    vision_turtle()
    show_turtles()
    countdown(10)
    turtle.tracer(1)
start_game_up()
turtle.mainloop()
