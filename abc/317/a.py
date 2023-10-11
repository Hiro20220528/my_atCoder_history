N, H, X = map(int, input().split())

A = list(map(int, input().split()))


b = 0
for i, n in enumerate(A, 1):
          if n + H >= X:
                    print(i)
                    break