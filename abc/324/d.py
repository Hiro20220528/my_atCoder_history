N = int(input())
S = input()

max_num = 0
for i in range(N):
          max_num += 9 * 10 ** i

moji = list(S)

history = {}
ans = 0
# あらかじめ計算する
for i in range(10**7):
          h = {}
          for num in moji:
                    h[num] = h.get(num, 0) + 1
          

          nijou = i**2
          if nijou > max_num:
                    break
          
          flag = True
          
          nijou_str = str(nijou)
          nijou_str = list(nijou_str)
          nijou_str = ['0'] * (N - len(nijou_str)) + nijou_str
          
          for chr in nijou_str:
                    if h.get(chr, 0) > 0:
                              h[chr] -= 1
                    else:
                              flag = False
                              break
                    
          if flag and history.get(nijou, True):
                    history[nijou] = False
                    ans += 1
                    
print(ans)
                    

