def demo(a,b,c=3,d=100):
    return sum((a,b,c,d))
print(demo(1,2,3,4))
print(demo(1,2,d=3))
