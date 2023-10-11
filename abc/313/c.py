N = int(input())

A = list(map(int, input().split()))

A.sort()

i = 0
while True:
          
          A[0] += 1
          A[-1] -= 1
          A.sort()
          
          result = A[-1] - A[0]
          # print(result)
          if result == 1 or result == 0:
                    break
          
          i += 1
          print(i)