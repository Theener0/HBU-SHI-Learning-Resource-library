from turtle import *
def jumpto(x,y):
    up()
    goto(x,y)
    down()
reset()
jumpto(-25,-25)
k=4
for i in range(k):
    forward(50)
    left(360/k)
exitonclick()
