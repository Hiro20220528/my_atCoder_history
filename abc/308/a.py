
A = list(map(int, input().split()))

standard = 0
flag = True
for i in A:
          if standard <= i:
                    standard = i
                    if i % 25 == 0:
                              if i >= 100 and i <= 675:
                                        # 処理を飛ばす
                                        continue
          flag = False
          # print(i)
          
print("Yes" if flag else "No")
          