N, M = map(int, input ().split())

A = [input().split() for _ in range(M)]

# 組み合わせの全パターンを考える
comb = {}
for i in range(N-1):
          person = str(i+1)
          for k in range(i + 1,N + 1):
                    next_person = str(k)
                    if person != next_person:
                              comb[person + next_person] = 0
                    # comb[next_person + person] = 0
# print(comb)

for row in A:
          for i in range(N-1):
                    person = row[i]
                    next_person = row[i + 1]
                    # print(person, next_person)
                    if int(person) > int(next_person):
                              comb[next_person+person] += 1
                    else:
                              comb[person+next_person] += 1
  
count = 0        
for value in comb.values():
          if value == 0:
                    count += 1
                    
print(count)