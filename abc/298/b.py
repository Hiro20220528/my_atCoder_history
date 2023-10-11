# N = int(input())

# A = [list(map(int, input().split())) for _ in range(N)]

# B = [list(map(int, input().split())) for _ in range(N)]

# # N = 2k + 1のとき、真ん中を比べる
# middle = N % 2
# if middle == 1:
#           # i,j は行列の真ん中
#           i = int(((N + 1) / 2) - 1)
#           j = int(((N + 1) / 2) - 1)
#           if A[i][j] != B[i][j]:
#                     print('No')

#           else:
#                     # Bと比べる
#                     count = 0
#                     acount = 0
#                     for i in range(N):
#                               for j in range(N):
#                                         if A[i][j] == 1 and B[i][j] == 1:
#                                                   count += 1
#                                         if B[i][j] == 1:
#                                                   acount += 1
                    
#                     # 3回回転させる
#                     for _ in range(3):
#                               if count == acount:
#                                         print('Yes')
#                                         break
#                               # 新規配列に入れる
#                               # A_rotated = [[0] * N] * N
#                               A_rotated = [[] for _ in range(N)]
#                               index_one = []
#                               for i in range(N):
#                                         for j in range(N):
#                                                   # A_rotated[i][j] = A[N-1-j][i]
#                                                   A_rotated[i].append(A[N-1-j][i])
#                                                   # タプルとして保存する
#                                                   if A_rotated[i][j] == 1:
#                                                             ij = (i, j)
#                                                             index_one.append(ij)
                              
#                               A = A_rotated
#                               # Bと比べる
#                               count = 0
#                               for index in index_one:
#                                         i = index[0]
#                                         j = index[1]
#                                         if B[i][j] != 1:
#                                                   break
#                                         else:
#                                                   count += 1
                                        
#                               if count == len(index_one):
#                                         print('Yes')
#                                         break
#                               if _ == 2 and count != len(index_one):
#                                         print('No')
# else:
#                     # Bと比べる
#                     count = 0
#                     acount = 0
#                     for i in range(N):
#                               for j in range(N):
#                                         if A[i][j] == 1 and B[i][j] == 1:
#                                                   count += 1
#                                         if B[i][j] == 1:
#                                                   acount += 1
                    
#                     # 3回回転させる
#                     for _ in range(3):
#                               if count == acount:
#                                         print('Yes')
#                                         break
#                               # 新規配列に入れる
#                               # A_rotated = [[0] * N] * N
#                               A_rotated = [[] for _ in range(N)]
#                               index_one = []
#                               for i in range(N):
#                                         for j in range(N):
#                                                   # A_rotated[i][j] = A[N-1-j][i]
#                                                   A_rotated[i].append(A[N-1-j][i])
#                                                   # タプルとして保存する
#                                                   if A_rotated[i][j] == 1:
#                                                             ij = (i, j)
#                                                             index_one.append(ij)
                              
#                               A = A_rotated
#                               # Bと比べる
#                               count = 0
#                               for index in index_one:
#                                         i = index[0]
#                                         j = index[1]
#                                         if B[i][j] != 1:
#                                                   break
#                                         else:
#                                                   count += 1
                                        
#                               if count == len(index_one):
#                                         print('Yes')
#                                         break
#                               if _ == 2 and count != len(index_one):
#                                         print('No')

N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]

B = [list(map(int, input().split())) for _ in range(N)]

A = [list(a)[::-1] for a in zip(*A)]

print(A)