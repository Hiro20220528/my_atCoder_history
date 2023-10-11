import sys
N = int(input())

A = list(map(int, input().split()))

if N == 1:
          print(0)
          sys.exit()

total = sum(A)

standard = total // N

# print(total / N)
# print(standard)

count = 0
plus = 0
minus = 0
for number in A:
          if number <= standard:
                    sa = standard - number
                    plus += sa
                    count += sa
          elif number > (standard+1):
                    
                    sa = number - (standard + 1)
                    minus += sa
                    count += sa
#           print(sa)
#           print(count)
#           print("--")

# if count % 2 == 0:
#           print(count // 2)   
# else:
#           print("-------")
#           print((count+1) // 2 )   
# # print(count // 2 + 1)
if plus >= minus:
          print(plus)
else:
          print(minus)
# print(plus, minus)