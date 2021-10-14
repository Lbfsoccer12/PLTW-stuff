#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
# draw spider body
spider.circle(20)
# configure spider legs

y = 70
anglelegs = 180 / 5

spider.pensize(5)
numofloop = 1

while (numofloop < 5):
  # draw spider legs
  spider.goto(0,20)
  
  spider.setheading(90 + (anglelegs*numofloop))
  
  spider.forward(y)
  numofloop = numofloop + 1

numofloop = 1

while (numofloop < 5):
  # draw spider legs
  spider.goto(0,20)
  spider.setheading(-90 + (anglelegs*numofloop))
  
  spider.forward(y)
  numofloop = numofloop + 1


spider.penup()
spider.goto(20,-1)
spider.pensize(10)
spider.pencolor("red")
spider.pendown()
spider.circle(5)
spider.penup()
spider.goto(-10,-1)
spider.pendown()
spider.circle(5)

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
