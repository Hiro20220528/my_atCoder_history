N = int(input())

A = list(map(int, input().split()))

search = {}
for i, num in enumerate(A):
          search[i+1] = num

# print(search)

# global 変数を定義
done = False

def dfs(i, flag, history):
          # print(f"{i}回目{flag}")
          if flag[i-1]:
                    if history[0] == i:
                              print(len(history))
                              print(*history)
                              global done
                              done = True
                              return True
                    else:
                              return False
          else:
                    flag[i-1] = True
                    history.append(i)
          
          dfs(search[i], flag, history)
          

for i in range(N):
          flag = [False for _ in range(N)]
          history = []
          dfs(i+1, flag, history)
          # print(done)
          if done:
                    break

                    