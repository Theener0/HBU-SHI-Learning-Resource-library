sn=100.0
hn=sn/2
for n in range(2,11):
    sn+=2*hn
    hn/=2
print('Total of road is %f'%sn)
print('The tenth is %f meter'%hn)
