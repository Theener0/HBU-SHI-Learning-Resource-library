n=0
for i in range(14700,14799+1):
    if i%57==0 or i%67==0:
        print('五位数是:',i)
        n=n+1
print('共有',n,'个')
