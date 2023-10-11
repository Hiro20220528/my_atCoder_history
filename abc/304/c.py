import math

n, d = map(int, input ().split())

maps = [list(map(int, input().split())) for _ in range(n)]

def distance(a1, b1, a2, b2):
          return math.sqrt( (a1 - b1) **2 + (a2 - b2) **2)

graph = [ [False] * n for _ in range(n)]

# print('graph')
# print(graph)

# グラフを作成する
for i in range(n):
          x = maps[i][0]
          y = maps[i][1]
          for k in range(n):
                    xi = maps[k][0]
                    yi = maps[k][1]
                    sa = distance(x, xi, y, yi)
                    if sa <= d:
                              graph[i][k] = True
                              
# print('graph')

# print(graph)

reached = {}
reached[0] = True

def dfs(reached, current):
          # print(reached)
          for i in range(n):
                    if current == i:
                              continue
                    # print(f'current: {current}, i: {i}')
                    if graph[current][i] and reached.get(i, False) == False:
                              reached[i] = True
                              # print(f'saiki:{i}')
                              dfs(reached, i)

dfs(reached, 0)

for i in range(n):
          if reached.get(i, False):
                    print("Yes")
          else:
                    print("No")
                    
