N = int(input())

S = list(input())

Q = int(input())

# A = [input().split() for _ in range(Q)]
A = [0 for _ in range(Q)]
index = None
s = None
for i in range(Q):
          t, x, c = input().split()
          t = int(t)
          if t == 2 or t == 3:
                    index = i
                    # A[i] = t
                    s = t
          if t == 1:
                    A[i] = [t, int(x)-1, c]

# print(index, s)
# print(A)

for i, e in enumerate(A):
          if i != index and e != 0:
                    x = e[1]
                    c = e[2]
                    S[x] = c
          elif i == index:
                    if s == 2:
                              S = [S[j].lower() for j in range(N)]
                    elif s == 3:
                              # S.upper()
                              S = [S[j].upper() for j in range(N)]
          
          
print(''.join(S))