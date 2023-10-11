H, W = map(int, input ().split())

A = [list(map(int, input().split())) for _ in range(H)]

for row in A:
          out = ''
          for num in row:
                    if num == 0:
                              out += '.'
                    else:
                              out += chr(64 + num)
          print(out)
                    