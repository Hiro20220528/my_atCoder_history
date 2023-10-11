all = [input().split() for _ in range(12)]

# print(*all)

# 0, 1に書き換える
bit_all = [None for _ in range(12)]
for i, row in enumerate(all):
          bit = [0 if num == '.' else 1 for num in list(row[0])]
          bit_all[i] = bit

# 4*4のグリッドを3つに分ける
grid_a = bit_all[:4]
grid_b = bit_all[4:8]
grid_c = bit_all[8:]

# print(grid_a)
# print('----')
# print(grid_b)
# print('----')
# print(grid_c)

# 1つのグリッドを左上まで持っていく
def init(grid):
          # 上にどれくらいいけるか
          up = 0
          for row in grid:
                    if sum(row) == 0:
                              up += 1
                    else:
                              break
          # 左にどれくらいいけるか
          left = 0
          # 転置して考える
          for row in zip(*grid):
                    # print(row, sum(row))
                    if sum(row) == 0:
                              left += 1
                    else:
                              break
                       
          # print(up, left)
          
          # 上にずらす
          grid = grid[up:] + grid[:up]
          # print(grid)
          # 左にずらす
          # 転置
          reverse_gird = []
          for row in zip(*grid):
                    reverse_gird.append(list(row))
          grid = reverse_gird[left:] + reverse_gird[:left]
          
          ans = []
          for row in zip(*grid):
                    ans.append(list(row))
          
          # print("===")
          # for k in ans:
          #           print(*k)
          # print(ans)
          
          return ans
                  
          
grid_a = init(grid_a)
grid_b = init(grid_b)
grid_c = init(grid_c)

# 三重ループで回せるだけ回す
# grid_aがどれくらい右と下にいけるか確認
def check_r_and_d(grid):
          down = 0
          for row in grid_a[::-1]:
                    if sum(row) == 0:
                              down += 1
                    else:
                              break
                    
          right = 0
          # 転置して考える
          r_grid_a = []
          for row in zip(*grid_a):
                    # print(row, sum(row))
                    r_grid_a.append(list(row))
                    
          for row in r_grid_a[::-1]:
                    if sum(row) == 0:
                              right += 1
                    else:
                              break
          # print(down, right)
          return down+1, right+1

adown, aright = check_r_and_d(grid_a)
bdown, bright = check_r_and_d(grid_b)
cdown, cright = check_r_and_d(grid_c)

def grid_down_one(grid):
          return grid[-1:] + grid[:len(grid) - 1]

def grid_down(grid, down):
          if down == 0:
                    return grid
          return grid[-down:] + grid[:len(grid) - down]

def grid_right(grid, right):
          # 転置して下にずらす
          r_grid = []
          for row in zip(*grid):
                    # print(row, sum(row))
                    r_grid.append(list(row))
          
          r_grid = grid_down_one(r_grid)
          # 元に戻す
          rr_grid = []
          for row in zip(*r_grid):
                    # print(row, sum(row))
                    rr_grid.append(list(row))
          return rr_grid

# grid_aについて
# print(grid_a)
for ad in range(adown):
          # 下にずらす
          print(ad, '---')
          if ad == 0:
                    grid_ad = grid_a
          else:
                    grid_ad = grid_down(grid_a, ad)
          for ar in range(aright):
                    print(ar)
                    if ar == 0:
                              grid_ar = grid_ad
                    else:
                              grid_ar = grid_right(grid_ad, ar)
                    # 右にずらす
                    for l in grid_ar:
                              print(*l)    
                              
                                 
                              
          #           print("----------")
                    # grid_bについて
                    # for bd in range(bdown):
                    #           for br in range(bright):
                    #                     for cd in range(cdown):
                    #                               for cr in range(cright):
                                                            
                    

                    
          