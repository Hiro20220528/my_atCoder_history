N, T = input().split()

N = int(N)

l = len(T)
# print(l)

S = ["" for _ in range(N)]

for i in range(N):
          S[i] = input().split()
          
ans = []
for index, each in enumerate(S):
          each = each[0]
          # print(each)
          each_l = len(each)
          
          # 長さが同じ
          # 文字も同じ
          # 1文字入れ替え
          if l == each_l:
                    if each == T:
                              # print("same", each)
                              ans.append(index+1)
                    else:
                              flag = True
                              count = 0
                              for j, moji in enumerate(each):
                                        if T[j] != moji:
                                                  count += 1
                                        if count > 1:
                                                  flag = False
                                                  break
                              if flag and count == 1:
                                        # print('1same', each)
                                        ans.append(index+1)
          
          # 長さが1小さい
          # Tから1文字削除
          elif each_l - 1 == l:
                    flag = True
                    count = 0
                    i = 0
                    j = 0
                    while j < l-1:
                              if T[i] != each[j]:
                                        count += 1
                                        j += 1
                              else:
                                        i += 1
                                        j += 1
                              if count > 1:
                                        flag = False
                                        break
                    if flag:
                              # print('1del', each)
                              ans.append(index+1)
                    
          # 長さが1大きい
          # Tに1文字追加
          elif each_l + 1 == l:
                    flag = True
                    
                    count = 0
                    i = 0
                    j = 0
                    while i < l-1:
                              # print(i, j, each, T)
                              if T[i] != each[j]:
                                        count += 1
                                        i += 1
                              else:
                                        i += 1
                                        j += 1
                              if count > 1:
                                        flag = False
                                        break
                    if flag:
                              # print('1add', each)
                              ans.append(index+1)
 
print(len(ans))
ans.sort()                       
print(*ans)



