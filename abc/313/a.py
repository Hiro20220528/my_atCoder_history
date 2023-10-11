import time

N = int(input())
          
A = list( map( int, input().split() ) )

sta = time.time()
p = A[0]
enemy = max(A)
end = time.time()
print(round((end - sta) * 1e6, 2))

sta = time.time()
local_max = max
t = A[0]

for i in range(N):
          # t = max(t, A[i])
          t = local_max(t, A[i])
end = time.time()

print(round((end - sta) * 1e6, 2))
