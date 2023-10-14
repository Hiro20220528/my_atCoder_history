N = int(input())

# N = 10 ** 18

# for i in range(1000):
#           if 2**i >= N:
#                     print(i)
#                     break
          
# for i in range(1000):
#           if 3**i >= N:
#                     print(i)
#                     break
          
# print("Finish")

flag = True
for x in range(60):
          for y in range(38):
                    if 2**x * 3**y == N:
                              flag = False
                              break
          if flag:
                    continue
          else:
                    break

if flag:
          print("No")
else:
          print("Yes")