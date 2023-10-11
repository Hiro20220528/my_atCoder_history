N, P, Q = map(int, input().split())

A = list(map(int, input().split()))

if (Q + min(A)) > P:
          print(P)
else:
          print(Q + min(A))