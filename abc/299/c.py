N = int(input())
S = input() 

o_list = S.split('-')
MAX = 0
for chr in o_list:
          if len(chr) > MAX:
                    MAX = len(chr)
   
if 'o' not in S or '-' not in S:
          print(-1)
else:                 
          print(MAX)