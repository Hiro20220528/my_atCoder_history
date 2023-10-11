# N回移動したい, M個の体力, 初期体力H, K未満なら体力がK回復する
N, M, H, K = map(int, input ().split())

# 移動する文字列
S = input() 

# x, y 座標に回復アイテムがある
items = [list(map(int, input().split())) for _ in range(M)]

used_item = {}

for item in items:
          ix = item[0]
          iy = item[1]
          used_item[(ix, iy)] = 1

arrive = True

# 初期座標
x = 0
y = 0

for i in range(N):
          move = S[i]
          
          if move == 'R':
                    x += 1
          elif move == 'L':
                    x -= 1
          elif move == 'U':
                    y += 1
          else:
                    y -= 1
          
          # 移動すると体力が1減る
          H -= 1
          if H < 0:
                    arrive = False
                    break
          
          position = [x, y]
          # print(items, 'items')
          # if position in items and H < K:
          if used_item.get((x, y), 0) == 1 and H < K:
                    used_item[(x, y)] = 0 
                    # index = items.index(position)
                    # print(index, 'index')
                    # items.pop(index)
                    H = K        
          
          
if arrive:
          print("Yes")
else:
          print("No")
                    