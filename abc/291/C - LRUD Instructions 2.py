N = int(input())

S = input()

visited = {}
def Check(S):
          x, y = 0, 0
          #  タプルにして集合に保存する
          xy = (x, y)
          visited[xy] = visited.get(xy, 0) + 1 
          for cha in S:
                    if cha == 'R':
                              x += 1
                    elif cha == 'L':
                              x -= 1
                    elif cha == 'U':
                              y += 1
                    else:
                              y -= 1
                    #  タプルにして集合に保存する
                    xy = (x, y)
                    visited[xy] = visited.get(xy, 0) + 1 
                    if visited[xy] >= 2:
                              return True
          return False
if Check(S):
          print('Yes')
else:
          print('No')