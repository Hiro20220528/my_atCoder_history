N, M = map(int, input().split())

nodes = [[None]*N for _ in range(N)]


for _ in range(M):
          node, next_node, c = map(int, input().split())
          nodes[node-1][next_node-1] = c
          nodes[next_node-1][node-1] = c
          
max_w = 0
def dfs(v, e):
          '''
          v はノード番号
          e はノードへの重みの合計
          max_w は重みの合計値
          history はすでに通ったノードの記録
          '''
          # print(v, 'node')
          # print(history)
          history[v-1] = True
          global max_w
          if e > max_w:
                    max_w = e
          
          # text = ''.join(history)
          for i in range(N):
                    w = nodes[v-1][i]
                    if w is None or history[i]:
                              continue
                    dfs(i+1, e + w)
                    
          history[v-1] = False
          
          
          
history = [False] * (N+1)
for i in range(N):
          
          dfs(i+1, 0)
          
print(max_w)

            
          
          