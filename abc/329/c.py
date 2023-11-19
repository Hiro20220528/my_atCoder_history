N = int(input())

S = input()
S += '-'
count = {}

before = S[0]
tmp_count = 1
for i in range(1, N+1):
    
    moji = S[i]
    if before == moji:
        tmp_count += 1
    else:
        if count.get(before, 0) < tmp_count:
            count[before] = tmp_count
        tmp_count = 1
        before = moji
        
total = 0
if len(count) == 0:
    total = 1
for num in count.values():
    total += num
print(total)
        
    
        
    


            