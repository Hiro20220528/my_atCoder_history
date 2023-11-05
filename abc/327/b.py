
# for e in range(10**9):
#     if e**e > 10 **18:
#         print(e)
#         print('Ok')
#         break

# 16 ** 16 > 10 **18となる

B = int(input())

flag = True
for e in range(1, 100):
    if e**e == B:
        flag = False
        print(e)
        break
if flag:
    print(-1)