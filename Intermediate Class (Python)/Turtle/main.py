import turtle
import colors
import random

franklin = turtle.Turtle()
franklin.shape("turtle")
franklin.hideturtle()

def drawTriangle(size, color):
  franklin.penup()
  franklin.color(color)
  
  franklin.pendown()
  for n in range(3):
    franklin.forward(size)
    franklin.left(120)
  franklin.penup()
  
def drawPolygon(size, sides):
  franklin.penup()
  franklin.home()
  franklin.color("blue")
  franklin.speed(0)
  franklin.pensize(5)
  
  franklin.pendown()
  
  for n in range(sides):
    franklin.forward(size)
    franklin.left(360 / sides)
    franklin.color(colors.randomRGBColor())
    
  franklin.penup()
  
def drawTriangleAbomination(quantity):
  franklin.penup()
  franklin.goto(-50, 0)
  franklin.color(colors.randomCommon())
  franklin.speed(0)
  franklin.pensize(1)
  
  franklin.pendown()
  
  for n in range(quantity):
    drawTriangle(200, colors.randomRGBColor())
    
    franklin.penup()
    franklin.setheading(270 + n)
    franklin.forward(1)
    franklin.left(90)
    franklin.pendown()
    
  franklin.penup()
  
drawTriangleAbomination(360)
