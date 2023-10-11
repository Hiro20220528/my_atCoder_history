N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]

def bfs(A, N):
          # Nが0なら終了
          if N == 0:
                    return
          
          return bfs(A, N - 1)

print(bfs(A, N))