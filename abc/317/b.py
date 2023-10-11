N = int(input())

A = list(map(int, input().split()))

A.sort()

for i in range(N-1):
          t = A[i]
          n = A[i+1]
          
          if n - t != 1:
                    print(t+1)
                    break