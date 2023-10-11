N = int(input())

hash = {}
def waru(num, k):
          print(hash)
          if num % 2 == 0:
                    waru(num // 2, 2*k)
          
          if num % 2 == 1 or num == 2:
                    hash[num] = hash.get(num, 0) + k
                    return 

for i in range(N):
          s, c = map(int, input().split())
          waru(s, c)
print(hash)
ans = 0
for key in hash.keys():
          if key == 1 or hash[key] == 1:
                    ans += 1
          else:
                    ans += 1

print(ans)

