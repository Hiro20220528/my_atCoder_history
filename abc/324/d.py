import itertools

N = int(input())
S = input()

moji = list(S)

p_list = list(itertools.permutations(moji))

h = {}
# あらかじめ計算する
for i in range(10**6):
          h[i**2] = True
          
ans = 0
for each in p_list:
          num = int(''.join(each))
          # print(num)
          if h.get(num, False):
                    h[num] = False
                    ans += 1
                    
print(ans)
                    

