#   a116_ladybug.py
import turtle as trtl


spider = trtl.Turtle()
spider.pensize(40)

legs = 6
y = 70
anglelegs = 380 / legs
print("z=", anglelegs)
spider.pensize(5)
numofloop = 0
print("z=", anglelegs)
while (numofloop < legs):
  spider.goto(0,-40)
  spider.setheading(anglelegs*numofloop)
  print("z*n=", numofloop*anglelegs)
  spider.forward(y)
  numofloop = numofloop + 1


# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)







# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
x = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (x < 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  xpos = ypos + 25
  xpos = xpos + 5
  x = x + 1

ladybug.hideturtle()


wn = trtl.Screen()
wn.mainloop()
