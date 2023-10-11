N, D, P = map(int, input().split())

F = list(map(int, input().split()))

F.sort(reverse=True)
# print(F)
plans = 0
count = 1
total = 0


for i in range(N):
          plans += F[i]

          if count == D or i == N - 1:
                    # print(plans)
                    if P > plans:
                              total += plans
                    else:
                              total += P
                    
                    plans = 0
                    count = 0
          
                    
          count += 1
          
print(total)
          