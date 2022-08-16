a=eval(input('请输入三角形边长:'))
import turtle
for i in range(3):
    turtle.seth(i*120)
    turtle.fd(a)

