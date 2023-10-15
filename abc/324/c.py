# N, T = input().split()

# N = int(N)

# l = len(T)
# # print(l)

# S = ["" for _ in range(N)]

# for i in range(N):
#           S[i] = input().split()
          
# ans = []
# for index, each in enumerate(S):
#           each = each[0]
#           # print(each)
#           each_l = len(each)
          
#           # 長さが同じ
#           # 文字も同じ
#           # 1文字入れ替え
#           if l == each_l:
#                     if each == T:
#                               # print("same", each)
#                               ans.append(indexndex+1)
#                     else:
#                               flag = True
#                               count = 0
#                               for j, moji in enumerate(each):
#                                         if T[j] != moji:
#                                                   count += 1
#                                         if count > 1:
#                                                   flag = False
#                                                   break
#                               if flag and count == 1:
#                                         # print('1same', each)
#                                         ans.append(indexndex+1)
          
#           # 長さが1小さい
#           # Tから1文字削除
#           elif each_l - 1 == l:
#                     flag = True
#                     count = 0
#                     i = 0
#                     j = 0
#                     while j < l-1:
#                               if T[i] != each[j]:
#                                         count += 1
#                                         j += 1
#                               else:
#                                         i += 1
#                                         j += 1
#                               if count > 1:
#                                         flag = False
#                                         break
#                     if flag:
#                               # print('1del', each)
#                               ans.append(indexndex+1)
                    
#           # 長さが1大きい
#           # Tに1文字追加
#           elif each_l + 1 == l:
#                     flag = True
                    
#                     count = 0
#                     i = 0
#                     j = 0
#                     while i < l-1:
#                               # print(i, j, each, T)
#                               if T[i] != each[j]:
#                                         count += 1
#                                         i += 1
#                               else:
#                                         i += 1
#                                         j += 1
#                               if count > 1:
#                                         flag = False
#                                         break
#                     if flag:
#                               # print('1add', each)
#                               ans.append(indexndex+1)
 
# print(len(ans))
# ans.sort()                       
# print(*ans)


N, Tdash = input().split()

A = [input().split() for _ in range(int(N))]

tdl = len(Tdash)

ans = []
for index, s in enumerate(A):
          s = s[0]
          ls = len(s)
          
          if s == Tdash:
                    # print('1', s)
                    ans.append(index+1)
                    continue

          # T' は、T(s) のいずれか 1 つの位置（先頭と末尾も含む）
          # に英小文字を 1 つ挿入して得られる文字列である。
          
          if tdl == 1 + ls:
                    i = 0
                    j = 0
                    onlyOne = 0
                    while i < tdl:
                              if s[j] != Tdash[i]:
                                        onlyOne += 1
                                        i+=1
                              else:
                                        i+=1
                                        j+=1
                              if j == ls:
                                        break
                    if onlyOne <= 1:
                              # print('2', s)
                              ans.append(index+1)
                    continue

          if ls - tdl == 1:
                    i = 0
                    j = 0
                    onlyOne = 0
                    while j < ls:
                              if s[j] != Tdash[i]:
                                        onlyOne += 1
                                        j+=1
                              else:
                                        i+=1
                                        j+=1
                                        
                              if i == tdl:
                                        break
                    if onlyOne <= 1:
                              # print('3', s)
                              ans.append(index+1)
                    continue
          
          if ls == tdl:
                    onlyOne = 0
                    for i, moji in enumerate(s):
                              if Tdash[i] != moji:
                                        onlyOne +=1
                    if onlyOne <= 1:
                              # print('4', s)
                              ans.append(index+1)
                    continue
          
print(len(ans))
print(*ans)