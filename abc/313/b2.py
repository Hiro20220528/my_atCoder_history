N, M = map(int, input().split())
# N 人, M個分の情報

yowai = [1 for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    yowai[b-1] = 0
    # g[a-1][b-1] = True
# print(yowai)
if sum(yowai) == 1:
    print(yowai.index(1)+1)
else:
    print(-1)
    
