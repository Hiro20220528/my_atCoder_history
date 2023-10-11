N = int(input())

A = list(map(int, input().split()))

p = A[0]
saikyo = 0
for i in range(1, N):
    saikyo = max(saikyo, A[i])
         
sa = saikyo - p + 1
if sa >= 1:
    print(sa)
else:
    print(0)
# print(p, saikyo)