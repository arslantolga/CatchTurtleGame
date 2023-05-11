import turtle
import time
from random import randint

score = 0

def position_control(x,y):
    # print(f"""
    # x kordinatı = {x_cor}
    # y kordinatı = {y_cor}
    # mouse x kordinatı = {x}
    # mouse y kordinatı = {y}
    # """)
    #
    # if (x_cor-20) <= int(x) <= (x_cor+20) and (y_cor-20) <= int(y) <= (y_cor+20):
    #     global score
    #     score = score + 1
    # print(score)
    pass

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Catch The Turtle Game")

turtle_instance = turtle.Turtle()

turtle_instance.shape("turtle")
turtle_instance.color("green")
turtle_instance.shapesize(3)
turtle_instance.penup()


for i in range(0,200):
    # x_cor = randint(-400, 400)
    # y_cor = randint(-300, 300)
    # turtle_instance.hideturtle()
    turtle_instance.setposition(i, i)
    # turtle_instance.showturtle()
    turtle_screen.onclick(position_control)
    time.sleep(10)

turtle_screen.mainloop()














