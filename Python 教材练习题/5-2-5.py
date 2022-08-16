g=2
def test():
    global g
    g=g+1
    return g
print(test())
print(g)
