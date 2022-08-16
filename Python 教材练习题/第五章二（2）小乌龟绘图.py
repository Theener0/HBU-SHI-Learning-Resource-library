from turtle import *
def jumpto(x,y):        #移动小乌龟不绘图
    up()
    goto(x,y)
    down()
reset()                #置小乌龟到原点处
colorlist = ['red','green','yellow']
for i in range(3):
    jumpto(-50,50-i*50)
    width(5*(i+1))
    color(colorlist[i]) #设置小乌龟属性
    forward(100)        #绘图
exitonclick()
