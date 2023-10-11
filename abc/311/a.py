N = int(input())

S = input() 

count = {}
flag = 3
for i, chr in enumerate(S):
          if count.get(chr, 0) == 0:
                    count[chr] = 1
                    flag -= 1
          if flag == 0:
                    print(i+1)
                    break
          