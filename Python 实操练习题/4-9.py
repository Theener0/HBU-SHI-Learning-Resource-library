"""
排列组合:1234组成的所有三位数
要求：
按以下输出规律进行输出。
1 2 3
1 2 4
1 3 2
1 3 4
1 4 2
1 4 3
2 1 3
2 1 4
2 3 1
2 3 4
2 4 1
......
提示：
输出采用print(i,j,k)，i、j、k分别表示三位数从左至右的每一位数
"""

for i in range(1,5):
      for j in range(1,5):
            for k in range(1,5):
                  if( i != k ) and (i != j) and (j != k):
                        print (i,j,k)