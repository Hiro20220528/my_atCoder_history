N = 9

block_list = [list(map(int, input().split())) for _ in range(N)]

def sudoku_row(array)->bool:
    for row in array:
        sudoku_hash = {}
        for number in row:
            if number not in sudoku_hash:
                sudoku_hash[number] = 1
            else:
                return False
    return True

flag = True
# 各行 o(9*9)
flag = sudoku_row(block_list)

# print('1', flag)
            

# 各列 o(9*9)
if flag:
    # 転置させる
    trans_block_list = [list(a) for a in zip(*block_list)]
    flag = sudoku_row(trans_block_list)

# print('flag', flag)

row_index = [0, -1, -1, -1, 0, 1, 1, 1]
column = [-1, -1, 0, 1, 1, 1, 0, -1]

# for t in trans_block_list:
#     print(*t)

# 3*3マス o(9*9*9)
if flag:
    for i in range(3):
        i *= 3
        i += 1
        for j in range(3):
            j *= 3
            # 9マス確認する
            sudoku_hash = {}
            
            j += 1
            # print('--------', i, j)
            middle = trans_block_list[i][j]
            sudoku_hash[middle] = True
            for k in range(8):
                # print(i+row_index[k], j+column[k])
                element = trans_block_list[i+row_index[k]][j+column[k]]
                # print(element)
                # print(sudoku_hash)
                if element not in sudoku_hash:
                    sudoku_hash[element] = True
                    # print('not -> ', element)
                else:
                    flag = False
                    break
                
            # print(flag)
            if not flag:
                break
        if not flag:
                break
            
            
if flag:
    print('Yes')
else:
    print('No')