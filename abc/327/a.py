N = int(input())

S = input()

before = S[0]
flag = False
for i, moji in enumerate(S):
    if i == 0:
        continue
    
    if before == 'a' and moji == 'b':
        flag = True
        break
    elif before == 'b' and moji == 'a':
        flag = True
        break
    
    before = S[i]
    
if flag:
    print('Yes')
else:
    print('No')