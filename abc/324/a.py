N = int(input())

A = list(map(int, input().split()))

k = A[0]
flag = True
for each in A:
          if k != each:
                    flag = False
                    break
          
if flag:
          print("Yes")
else:
          print("No")