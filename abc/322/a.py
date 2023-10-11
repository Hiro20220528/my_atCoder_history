N = int(input())

S = input() 

base = ['A', 'B', 'C']
index = 0
ans = 0
result = False
for moji in S:
          ans += 1
          # print(moji)
          if moji == base[index]:
                    # print("match")
                    index += 1
          elif moji == base[0]:
                    # print("false")
                    index = 1
          else:
                    index = 0
                    
          if index == 3:
                    # print(ans)
                    result = True
                    break
          
if result:
          print(ans-2)
else:
          print(-1)