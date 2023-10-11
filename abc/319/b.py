N = int(input())

ans = ''
for i in range(N+1):
          s = 100
          for j in range(1, 10):
                    if N % j == 0 and (j * i) % N == 0:
                              s = min(s, j)
          if s == 100:
                    ans += '-'
          else:
                    ans += str(s)
                    
print(ans)  
                    