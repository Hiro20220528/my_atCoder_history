N = int(input())

A = list(map(int, input().split()))

index = 0
k = 0
result = [0 for _ in range(N)]
for number in A:
          result[k] += number
          if index == 6:
                    index = 0
                    k += 1
          else:
                    index += 1
                    
print(*result)