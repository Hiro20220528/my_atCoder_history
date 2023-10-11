import sys

N, M = map(int, input().split())

if N - M > 1:
          print(-1)
          sys.exit()

hash = {}
for _ in range(M):
          key, value = map(int, input().split())
          if hash.get(key) is None:
                    hash[key] = [value]
          else:
                    hash[key].append(value)
                    

# print(hash)

flag = False
def recursion(key, array):
          # try:
          #           array.remove(key)
          # except:
          #           pass
          array[key-1] = 0
          
          # if len(array) == 0:
          if sum(array) == 0:
                    global flag
                    flag = True
                    return
          
          # print(key, array, 'key')
          
          if hash.get(key) is None:
                    return
          else:
                    for j in hash[key]:
                              # print(j, array, 'j')
                              recursion(j, array)
          
for i in range(1, N+1):
          result = {}
          recursion(i, [1 for i in range(N)])
          if flag:
                    print(i)
                    break

if not flag:
          print(-1)