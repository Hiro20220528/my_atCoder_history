import sys

H, W = map(int, input ().split())

S = [input().split() for _ in range(H)]
# print("-")
# print(S)
# print("-")
# まずは探索
for row in range(len(S)):
          column = S[row][0].find('snuke')
          if  column > -1:
                    for i in range(5):
                              print(row + 1, column + i+1)
                              
                    sys.exit()
# 斜め
for i in range(H - 4):
          moji = ''
          for k in range(W - i):
                    moji += S[i + k][0][k]
                    
          column = moji.find('snuke')
          if  column > -1:
                    for j in range(5):
                              print(i + j, column + 1 + j)
                    sys.exit()
          moji = "".join(list(reversed(moji)))
          column = moji.find('snuke')
          if  column > -1:
                    for j in range(5):
                              print(H - (i + j), W - (column + j))
                    sys.exit()
# ひっくり返る
# print("--")
l = []
for row in S:
          l.append(list(reversed(row[0])))
# print("-------")
l = [''.join(x) for x in l]
# print(l)
# print("S: reverse")
# まずは探索
for row in range(len(l)):
          # print(l[row])
          column = l[row].find('snuke')
          # print(column)
          if  column > -1:
                    for i in range(5):
                              print(row + 1, W - (column + i))
                              
                    sys.exit()  
# print("斜め")
# print(l)  
# 斜め  
for i in range(H - 4):
          moji = ''
          for k in range(W - i):
                    moji += l[i + k][k]
                    
          column = moji.find('snuke')
          if  column > -1:
                    for j in range(5):
                              print(i + j, column + 1 + j)
                    sys.exit()
          moji = "".join(list(reversed(moji)))
          column = moji.find('snuke')
          if  column > -1:
                    for j in range(5):
                              print(H - (i + j), W - (column + j))
                    sys.exit()        
      
# 転置させる
s = [list(x[0]) for x in S]
t = [list(x) for x in zip(* s)]
t = [''.join(x) for x in t]
for row in range(len(t)):
          column = t[row].find('snuke')
          if  column > -1:
                    for i in range(5):
                              print(column + i+1, row + 1)
                              
                    sys.exit()
# print("***")
# print(t)
# 斜め  
for i in range(H - 4):
          moji = ''
          for k in range(W - i):
                    moji += t[i + k][k]
                    
          column = moji.find('snuke')
          if  column > -1:
                    for j in range(5):
                              print(i + j, column + 1 + j)
                    sys.exit()
          moji = "".join(list(reversed(moji)))
          column = moji.find('snuke')
          if  column > -1:
                    for j in range(5):
                              print(H - (i + j), W - (column + j))
                    sys.exit()
# print("&&&")
l = []
for row in t:
          l.append(list(reversed(row)))
l = [''.join(x) for x in l]
# print(l)
# print("t: reverse")
for row in range(len(l)):
          column = l[row].find('snuke')
          if  column > -1:
                    for i in range(5):
                              print(H - (column + i), row + 1)
                              
                    sys.exit()

# 斜め探索
# print(S)
for i in range(H - 4):
          moji = ''
          for k in range(W - i):
                    moji += l[i + k][k]
                    
          column = moji.find('snuke')
          if  column > -1:
                    for j in range(5):
                              print(i + j, column + 1 + j)
                    sys.exit()
          moji = "".join(list(reversed(moji)))
          column = moji.find('snuke')
          if  column > -1:
                    for j in range(5):
                              print(H - (i + j), W - (column + j))
                    sys.exit()
      
# print(s)              

                    
          