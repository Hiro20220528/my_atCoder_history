S = input()
# s = list(S)
flag = True
for i, moji in enumerate(S):
          i+= 1
          if i % 2 == 0 and moji == '1':
                    # print(i, moji)
                    flag = False
                    
if flag:
          print("Yes")
else:
          print("No")