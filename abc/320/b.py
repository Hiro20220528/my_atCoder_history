S = input()

# 回文であるものの長さの最大値を求める

# 大きい順から調べる

def check(s, num):
          for i in range(len(s) - num + 1):
                    a = s[i:i+num]
                    if a == a[::-1]:
                              print(len(a))
                              return
                    
          check(s, num-1)
check(S, len(S))
                    
          
          