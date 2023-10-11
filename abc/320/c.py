M = int(input())
S1 = input() 
S2 = input() 
S3 = input() 

a1 = list(S1*2)
a2 = list(S2*2)
a3 = list(S3*2)

ahash = {}
bhash = {}
chash = {}
# 全探索で間に合う
for i, (s1, s2, s3) in enumerate(zip(a1, a2, a3)):
          # print(i, s1, s2, s3)
          
          ahash[s1] = ahash.get(s1, []) + [(i, 'a')]
          bhash[s2] = bhash.get(s2, []) + [(i, 'b')]
          chash[s3] = chash.get(s3, []) + [(i, 'c')]

# print(ahash)
min_i = 400
for i in range(10):
          flag = {}
          flag['a'] = 0
          flag['b'] = 0
          flag['c'] = 0
          r = [False for _ in range(400)]
          if ahash.get(f"{i}", []) == [] or bhash.get(f"{i}", []) == [] or chash.get(f"{i}", []) == []:
                    continue
          tmp = ahash[f"{i}"] + bhash[f"{i}"] + chash[f"{i}"]
          tmp.sort()
          print(tmp)
          for j, s in tmp:
                    if flag[s] == 0 and r[j] == False:
                              r[j] = True
                              flag[s] = 1
                    
                    if flag['a'] == 1 and flag['b'] == 1 and flag['c'] == 1:
                              min_i = min(min_i, j)
                              # print(i, min_i)
                              break
       
if min_i == 400:
          print(-1)
else:   
          print(min_i)
          