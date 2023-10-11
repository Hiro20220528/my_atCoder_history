N, M = map(int, input().split())

A = list(map(int, input().split()))

S = [0 for _ in range(N)]

for i in range(N):
          S[i] = input()
          
score = [0 for _ in range(N)]

o = [[0 for _ in range(M)] for _ in range(N)]



for k, each in enumerate(S):
          for j, t in enumerate(each):
                    if t == 'o':
                              score[k] += A[j]
                    else:
                              o[k][j] = A[j]
                              
                              
          score[k] += k+1


m = max(score)
# A.sort(reverse=True)

# print(o)

ans = [0 for _ in range(N)]
for num in range(N):
          o[num].sort(reverse=True)
          i = 0
          
          # print(m)
          while True:
                    # print(score[num], o)
                    if score[num] >= m:
                              break
                    ans[num] += 1
                    score[num] += o[num][i]
                    i += 1
          # print("----")
                    
for a in ans:
          print(a)