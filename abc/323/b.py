N = int(input())

A = [input().split() for _ in range(N)]
# print(A)
team = {}
for j, i in enumerate(A):
          tmp = 0
          for k, each in enumerate(i[0]):
                    # print(k, each)
                    if each == 'o':
                              tmp += 1
          if team.get(tmp, False):   
                    team[tmp] = team[tmp] + [j+1]
          else:
                    team[tmp] = [j+1]
                              
# print(team)

ans = []
for score in range(N+1):
          
          score = N - score
          # print(score)
          if team.get(score, False):
                    for i in team[score]:
                              ans.append(i)
                    
print(*ans)