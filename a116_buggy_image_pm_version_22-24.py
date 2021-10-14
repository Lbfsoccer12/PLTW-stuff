#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
# draw spider body
spider.circle(20)
# configure spider legs
legs = 6
y = 70
anglelegs = 380 / legs
print("z=", anglelegs)
spider.pensize(5)
numofloop = 0
print("z=", anglelegs)
while (numofloop < legs):
  # draw spider legs
  spider.goto(0,0)
  spider.setheading(anglelegs*numofloop)
  print("z*n=", numofloop*anglelegs)
  spider.forward(y)
  numofloop = numofloop + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
