# import sys

H, W = map(int, input().split())

grid = [input().split() for _ in range(H)]

if H == 1 and W == 1:
          print(1, 1)
          # sys.exit()
elif H == 1 and W != 1:
          index = grid[0][0].index('.')
          print(1, index + 1)
elif W == 1 and H != 1:
          for i in range(len(grid)):
                    if grid[i][0] == '.':
                              print(i + 1, 1)
                              break
else:
          for i in range(len(grid) -  1):       
                    num = 0
                    for k, (a, b) in enumerate(zip(grid[i][0], grid[i + 1][0])):
                              # print(k, a, b)
                              if a != b:
                                        num += 1
                    if num == 1:
                              index = i
                              for j in range(W):
                                        top = grid[index][0][j]
                                        down = grid[index + 1][0][j]
                                        if top != down:
                                                  if top == '.':
                                                            print(index + 1, j + 1)
                                                  else:
                                                            print(index + 2, j + 1)
                                                  break
                              break
                                        

          

                    