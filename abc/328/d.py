S = input()

match = 'ABC'

ans = ''
for moji in S:
    ans += moji
    
    if len(ans) >= 3 and ans[-3:] == match:
        ans = ans[:-3]
    
print(ans)
        