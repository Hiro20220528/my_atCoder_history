N, M = map(int, input ().split())

A = list(map(int, input().split()))

B = list(map(int, input().split()))

count = 1
i, j = 0, 0
out_A, out_B = [], []
if N < M:
          while i < N:
                    if A[i] < B[j]:
                              out_A.append(count)
                              i += 1
                    else:
                              out_B.append(count)
                              j += 1
                              
                    count += 1
          [out_B.append(count + k) for k in range(M - N)]
else:
          while j < M:
                    if A[i] < B[j]:
                              out_A.append(count)
                              i += 1
                    else:
                              out_B.append(count)
                              j += 1
                              
                    count += 1
                    
          [out_A.append(count + k) for k in range(N - M)]
          

for num in out_A:
          print(num, end=' ')
for num in out_B:
          print(num, end=' ')