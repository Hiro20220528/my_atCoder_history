N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

# x_reverse = list(map(list, zip(*A)))

def check(A):
          for i in range(N):
                    s = A[i]
                    for k, a in enumerate(A):
                              if i == k:
                                        continue
                              if s[0] >= a[0] and {*a[2:]} >= {*s[2:]}:
                                       if {*a[2:]} > {*s[2:]} or s[0] > a[0]:
                                        #          print(s, a)
                                                 return print("Yes")
                              # elif {*a[2:]} < {*s[2:]}:
                              #           # print(a[2:], s[2:])
                              #           # print(i, '--------', index, k)
                              #           return print("Yes")
                              
                                        
          return print("No")
# def check(x_reverse, A):
#           for i in range(N):
#                     min_A = min(x_reverse[0])
#                     index = x_reverse[0].index(min_A)
#                     x_reverse[0][index] = 1000000000
                    
#                     s = A[index]
#                     print(s, x_reverse[0])
#                     # print(a[2:], s[2:])
#                     for k, a in enumerate(A):
#                               if k == index or x_reverse[0][k] == 1000000000:
#                                         # print(i, index)
#                                         continue
#                               elif {*a[2:]} < {*s[2:]}:
#                                         # print(a[2:], s[2:])
#                                         # print(i, '--------', index, k)
#                                         return print("Yes")
                              
                                        
#           return print("No")

check(A)