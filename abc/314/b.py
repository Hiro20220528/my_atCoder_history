N = int(input())

# A = [list(map(int, input().split())) for _ in range(N)]

pton = {}
ntop = {}
for i in range(N):
          c = int(input())
          
          A = list(map(int, input().split()))
          i += 1
          
          pton[i] = A
          
          for k in A:
                    if ntop.get(k, False):
                              ntop[k].append(i)
                    else:
                              ntop[k] = [i]
                              
x = int(input())

result = 100
answer = []
if ntop.get(x, False):
          pl = ntop[x]
          for p in pl:
                    l = len(pton[p])
                    if l < result:
                              result = l
                              answer = [p]
                    elif l == result:
                              answer.append(p)
          print(len(answer))
          answer.sort()
          print(*answer)
else:
          print(0)
                              
# print(pton)

# print(ntop)
          
          