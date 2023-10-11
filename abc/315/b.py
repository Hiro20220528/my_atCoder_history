N = int(input())

A = list(map(int, input().split()))

ave = (sum(A) + 1) / 2

# print(ave)

for i, days in enumerate(A):
          if ave - days > 0:
                    ave -= days
          else:
                    print(i + 1, int(ave))
                    break