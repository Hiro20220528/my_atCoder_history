N = int(input())

S = input() 

T = input() 

similar = True

for i in range(N):
          s = S[i]
          t = T[i]
          # print(s, t)
          if s == t:
                    # print(0)
                    similar = True
          elif (s == '1' and t == 'l'):
                    # print(1)
                    similar = True
          elif (t == '1' and s == 'l'):
                    # print(2)
                    similar = True
          elif (s == '0' and t == 'o'):
                    # print(3)
                    similar = True
          elif (s == 'o' and t == '0'):
                    # print(4)
                    similar = True
          else:
                    # print(5)
                    similar = False
                    break
if similar:
          print("Yes")
else:
          print("No")
          