"""
题目:求累加运算中满足条件的n值    
 	
题目内容：
注意：临界值的计算。
已知s=2+4+6+8+…+n，求使得s不大于100时的最大n值
"""

"""
if __name__ == "__main__":
      sum = 0
      for i in range(2,100,2):
            sum += i
            if sum >= 100:
                  print(i-2)
                  break
  
"""

from math import *
i=2
s=2
while s<=100:
      i+=2
      s+=i

print(i-2)