import turtle
import time
from random import randint

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Catch The Turtle Game")
turtle_screen.setup(1000,700)

turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("green")
turtle_instance.shapesize(3)
turtle_instance.penup()
class MyTurtle():
    def __init__(self,x_cor=0,y_cor=0,zorluk=0,score=0):
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.zorluk = zorluk
        self.score = score
    def position_control(self, x, y):
        self.x_cor = x
        self.y_cor = y
        return self.x_cor , self.y_cor
    def score_control(self):
        pass


Game_turtle = MyTurtle()

# while True:
#     rand_x_cor = randint(-200, 200)
#     rand_y_cor = randint(-200, 200)
#     turtle_instance.hideturtle()
#     turtle_instance.goto(rand_x_cor, rand_y_cor)
#     turtle_screen.listen()
#     turtle_screen.onscreenclick(Game_turtle.position_control)
#     print(Game_turtle.x_cor,Game_turtle.y_cor)
#     print(rand_x_cor,rand_y_cor)
#
#     turtle_instance.showturtle()
#     time.sleep(3)

rand_x_cor = randint(-200, 200)
rand_y_cor = randint(-200, 200)
turtle_instance.hideturtle()
turtle_instance.goto(rand_x_cor, rand_y_cor)
turtle_screen.listen()
turtle_screen.onscreenclick(Game_turtle.position_control)
print(Game_turtle.x_cor,Game_turtle.y_cor)
print(rand_x_cor,rand_y_cor)

turtle_instance.showturtle()




turtle.mainloop()




