N, M = map(int, input().split())

S = input()
T = input()

l = len(T)
if S[:l] != T or S[-l:] != T:
    print('No')
else:
    if set(S) != set(T):
        print('No')
    else:
        print("Yes")