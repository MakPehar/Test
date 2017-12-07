import turtle
import random
import math
class Player:
    def __init__(self):
        self.tt = turtle.Turtle()
        self.tt.speed(0)
        self.tt.penup()
        self.tt.color("green")
        self.running = True
        self.speed = 0
    def Turning(self):
        turtle.listen()
        turtle.onkey(self.turnleft, "Left")  # These two keybindings turn the turtle left
        turtle.onkey(self.turnleft, "a")
        turtle.onkey(self.turnright, "Right")  # These two keybindings turn the turtle right
        turtle.onkey(self.turnright, "d")
        turtle.onkey(self.speeden, "Up")  # These two keybindings speed up the turtle
        turtle.onkey(self.speeden, "w")
        turtle.onkey(self.slowdown, "Down")  # These two keybindings slow the turtle down
        turtle.onkey(self.slowdown, "s")
        turtle.onkey(self.stop, "Escape")
    def turnleft(self):
        self.tt.left(10)
    def turnright(self):
        self.tt.right(10)
    def speeden(self):
        if self.speed < 50:
            self.speed += 1
    def slowdown(self):
        if self.speed > 0:
            self.speed -= 1
    def stop(self):
        self.running = False
class Enemy:
    def __init__(self):
        self.turt = turtle.Turtle()
        self.turt.color("red")
        self.turt.shape("circle")
        self.turt.penup()
        self.turt.speed(0)
        self.speed = random.randint(1, 10)
        self.direction = random.randint(0,360)
class ScoreTurtle:
    def __init__(self):
        self.scoreturtle = turtle.Turtle()
        self.scoreturtle.hideturtle()
        self.scoreturtle.color("white")
        self.scoreturtle.penup()
        self.scoreturtle.setposition(-290, 310)
        self.scoreturtle.speed(0)
        self.scoreturtle.pendown()
class MainGame:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.tracer(8)
        self.window.bgcolor("black")
        self.trt = Player()
        self.scortle = ScoreTurtle()
        self.goals = []
        self.maximumgoals = 6
        for i in range(self.maximumgoals):
            self.goals.append(Enemy())
            self.goals[i].turt.setposition(random.randint(-(self.window.window_width() / 2) + 5, self.window.window_width() / 2 - 5),random.randint(-(self.window.window_height()/2)+5, self.window.window_height()/2-5))
            self.goals[i].turt.right(self.goals[i].direction)
        self.speed = 0
        self.score = 0
        self.running = True
        self.scorestring = "Your score is: %s" % self.score
        self.scortle.scoreturtle.write(self.scorestring, False, align="left", font=("Arial", 14, "normal"))
        self.Running()
    def CheckCollision(self,t1,t2):
        self.d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
        if self.d < 15:
            return True
        else:
            return False
    def Running(self):
        turtle.listen()
        while self.running:
            self.trt.Turning()
            if self.trt.tt.xcor() < -(self.window.window_width() / 2) + 5:
                self.trt.tt.back(self.trt.speed)
                self.trt.tt.right(180)
            if self.trt.tt.xcor() > self.window.window_width() / 2 - 5:
                self.trt.tt.back(self.trt.speed)
                self.trt.tt.left(180)
            if self.trt.tt.ycor() > self.window.window_height() / 2 - 5 or self.trt.tt.ycor() < -(self.window.window_height() / 2) + 5:
                self.trt.tt.back(self.trt.speed)
                self.trt.tt.left(180)
            self.trt.tt.forward(self.trt.speed)
            self.running = self.trt.running
            for count in range(self.maximumgoals):
                # This checks collision between the turtle we control and the goal and adds to the goal
                if self.CheckCollision(self.trt.tt, self.goals[count].turt):
                    self.goals[count].turt.hideturtle()
                    self.goals[count].turt.setposition(
                        random.randint(-(self.window.window_width() / 2) + 5, self.window.window_width() / 2 - 5),
                        random.randint(-(self.window.window_height() / 2) + 5, self.window.window_height() / 2 - 5))
                    self.goals[count].turt.right(random.randint(0, 360))
                    self.goals[count].speed = random.randint(1,10)
                    self.goals[count].turt.showturtle()
                    self.score += 1
                    self.scortle.scoreturtle.undo()
                    self.scortle.scoreturtle.setposition(-290, 310)
                    self.scorestring = "Your score is: %s" % self.score
                    self.scortle.scoreturtle.write(self.scorestring, False, align="left", font=("Arial", 14, "normal"))
                self.goals[count].turt.forward(self.goals[count].speed)  # Making the goal move
                # Checking whether the goals' are in the boundry
                if self.goals[count].turt.xcor() < -(self.window.window_width() / 2) + 5:
                    self.goals[count].turt.back(self.goals[count].speed)
                    self.goals[count].turt.right(180)
                if self.goals[count].turt.xcor() > self.window.window_width() / 2 - 5:
                    self.goals[count].turt.back(self.goals[count].speed)
                    self.goals[count].turt.right(180)
                if self.goals[count].turt.ycor() > self.window.window_height() / 2 + 10 or self.goals[count].turt.ycor() < -(self.window.window_height() / 2) - 10:
                    self.goals[count].turt.back(self.goals[count].speed)
                    self.goals[count].turt.left(180)

mak = MainGame()