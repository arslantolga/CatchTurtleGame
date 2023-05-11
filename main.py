import turtle
import time
from random import randint

score = 0
t = 20
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Catch The Turtle Game")

turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("green")
turtle_instance.shapesize(3)
turtle_instance.penup()

turtle_instance2 = turtle.Turtle()
turtle_instance2.color("green")
turtle_instance2.shapesize(3)
turtle_instance2.penup()
turtle_instance2.hideturtle()
turtle_instance2.goto(0,300)

def position_control(x,y):
    x_cor, y_cor = turtle_instance.position()
    print(f"""
    x kordinatı = {x_cor}
    y kordinatı = {y_cor}
    mouse x kordinatı = {x}
    mouse y kordinatı = {y}
    """)

    if (x_cor-20) <= int(x) <= (x_cor+20) and (y_cor-20) <= int(y) <= (y_cor+20):
        global score
        score = score + 1
        print("Catch")
    print(score)


def start_game():
    for i in range(0, 200):
        x_cor = randint(-400, 400)
        y_cor = randint(-300, 300)
        turtle_instance.hideturtle()
        turtle_instance.goto(x_cor, y_cor)
        turtle_screen.listen()
        turtle_screen.onscreenclick(position_control)
        turtle_instance.showturtle()
        printing()
        time.sleep(1)

def closing_game():
    turtle_screen.bye()

def printing():
    message = f"""
            Score : {score}
            Time : 
            """
    turtle_instance2.clear()
    turtle_instance2.write(message, align="center", font=("Arial", 12, "bold"))

turtle_screen.listen()
turtle_screen.onkey(fun=start_game,key="s")
turtle_screen.onkey(fun=closing_game,key="q")

while t >= 0:
    t -= 1


turtle_screen.mainloop()















