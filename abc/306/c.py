N = int(input())

A = list(map(int, input().split()))


count = {}
pton = {}
place = [0 for _ in range(len(A) // 3)]
index = 0
for k, number in enumerate(A):
          if count.get(number, None) is None:
                    count[number] = 1
                    
          elif count[number] == 1:
                    # 2回目以降なので場所を記録する
                    count[number] += 1
                    pton[k + 1] = number 
                    place[index] = k + 1
                    index += 1

place.sort()

result = [0 for _ in range(N)]
for k, num in enumerate(place):
          result[k] = pton[num]
          
print(*result)