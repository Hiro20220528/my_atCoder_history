# H, W = map(int, input().split())

# sensors_list = [input().split() for _ in range(H)]
# # sensors_listを分割する
# sensors_list = [list(each[0]) for each in sensors_list]
# # print(sensors_list)

# history = [[False for _ in range(W)] for _ in range(H)]
# # print(*history)

# # 深さ優先探索で検索していき探索したところはTrueにしていく

# def dfs(state, i, j):
#     if i < 0 or H <= i:
#         return
#     if j < 0 or W <= j:
#         return
    
#     # 周りの6面を見てあれば再帰的にdfsを呼び出す
#     if history[i][j]:
#         return
    
#     history[i][j] = True # すでに探索済み
    
#     if state == '.':
#         return 
    
#     # print(i, j)
    
        
    
#     # 6面を確認する
#     if i - 1 >= 0:
#         u = sensors_list[i-1][j]
#         dfs(u, i-1, j)
#         if j - 1 >= 0:
#             ul = sensors_list[i-1][j-1]
#             dfs(ul, i-1, j-1)
#         if j + 1 < W:
#             ur = sensors_list[i-1][j+1]
#             dfs(ur, i-1, j+1)
            
#     if j - 1 >= 0:
#         l = sensors_list[i][j-1]
#         dfs(l, i, j-1)
        
#     if j + 1 < W:
#         r = sensors_list[i][j+1]
#         dfs(r, i, j+1)
        
#     if i + 1 < H:
#         d = sensors_list[i+1][j]
#         dfs(d, i+1, j)
#         if j - 1 >= 0:
#             dl = sensors_list[i+1][j-1]
#             dfs(dl, i+1, j-1)
#         if j + 1 < W:
#             dr = sensors_list[i+1][j+1]
#             dfs(dr, i+1, j+1)

# count = 0
# for i in range(H):
#     for j in range(W):
#         block = sensors_list[i][j]
#         if block == '#' and history[i][j] == False:
#             count += 1
#             # print("ok")
#         # elif history[i][j] == False:
#         # print(history)
#         dfs(block, i, j)
        
# print(count)
        
        
H, W = map(int, input().split())

sensors_list = [input().split() for _ in range(H)]
sensors_list = [list(each[0]) for each in sensors_list]

history = [[False for _ in range(W)] for _ in range(H)]

# あらかじめ周りを定義しておく
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 方針
# dfsの中で周りを見てそこを探索済みにしていく。
# 探索がないもので # の数を数える

print(history, sensors_list)

def dfs(x, y):
    if (x < 0 or x >= H) or (y < 0 or y >= W):
        # print('return', x, y)
        return
    
    if history[i][j] or sensors_list[i][j] == '.':
        return
    
    history[x][y] = True
    
    print(x, y)
    
    for index in range(8):
        x += dx[index]
        y += dy[index]
        # print(x, y)
        # print("+++++++++")
        dfs(x, y)
    
ans = 0
for i in range(H):
    for j in range(W):
        # もし、訪れてなくて # なら +1
        # print(history)
        if history[i][j] == False and sensors_list[i][j] == '#':
            ans += 1
            # print(i, j)
            # print('-----')
            dfs(i, j)
print(history)
print(ans)
    