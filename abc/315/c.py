N = int(input())

f, s = map(int, input().split())
f_2, s_2 = map(int, input().split())

if f == f_2:
          max_f = f
          max_s = max(s, s_2)
          max_value = max(s, s_2) + min(s, s_2)/2
else:
          if f > f_2:
                    max_f = f
                    max_s = s
                    max_value = s + s_2
          else:
                    max_f = f_2
                    max_s = s_2
                    max_value = s + s_2
                    
for i in range(N-2):
          f, s = map(int, input().split())
          
          if f == max_f:
                    tmp = max(max_value, max(max_s, s) + min(max_s, s)/2)
                    if tmp >= max_value:
                              max_s = max(max_s, s)
                              max_value = tmp
          else:
                    tmp = max(max_value, max_s + s)
                    if tmp >= max_value:
                              if max_s != max(max_s, s):
                                        max_s = s
                                        max_f = f
                              max_value = tmp
          # print(max_value)
                              
print(int(max_value))
                    
                              
          
          