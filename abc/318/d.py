N = int(input())

nodes = [[None] * N for _ in range(N)]

A = [list(map(int, input().split())) for _ in range(N-1)]

for i, row in enumerate(A):
          for j, node in enumerate(row):
                    nodes[i][j+i+1] = node
                    nodes[j+i+1][i] = node
 
# for node in nodes:
                            
#           print(node)


max_w = 0
def dfs(v, e, flag):
          '''
          v はnode番号
          e は重みの合計
          '''
          # print(v, e, flag)
          history[v] = False
          
          global max_w
          max_w = max(e, max_w)

          for node, w in enumerate(nodes[v]):
                    if w is None or history[node] == False:
                              continue
                    if flag:
                              flag = False
                              next_w = w + e
                    else:
                              flag = True
                              next_w = w
                    if history[node]:
                              dfs(node, next_w, flag)
          
          
          
for i in range(N):
          history = [True] * N
          flag = True
          dfs(i, 0, flag)
print(max_w)