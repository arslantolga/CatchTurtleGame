import turtle
import time
from random import randint

def score(*args):
    return args

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Catch The Turtle Game")

turtle_instance = turtle.Turtle()

turtle_instance.shape("turtle")
turtle_instance.color("green")
turtle_instance.shapesize(3)
turtle_instance.penup()

turtle_screen.listen()
turtle_screen.onclick(fun=score,btn=1,add=None)

print(list)



turtle_screen.mainloop()



#def score():

# turtle_screen = turtle.Screen()
# turtle_screen.bgcolor("light blue")
# turtle_screen.title("Catch The Turtle Game")
#
# turtle_instance = turtle.Turtle()
#
# turtle_instance.shape("turtle")
# turtle_instance.color("green")
# turtle_instance.shapesize(3)
# turtle_instance.penup()
#
#
# while True:
#     x_cor = randint(-400, 400)
#     y_cor = randint(-300, 300)
#     turtle_instance.hideturtle()
#     turtle_instance.setposition(x_cor, y_cor)
#     turtle_instance.showturtle()
#     time.sleep(0.3)
#
#
# turtle_screen.mainloop()





















