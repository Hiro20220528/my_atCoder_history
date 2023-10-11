# 整数N
N = int(input())

# 5N人の特典
X = list(map(int, input().split()))

# 最小値をN回削除
[X.remove(min(X)) for _ in range(N)]

# 最大値をN回削除
[X.remove(max(X)) for _ in range(N)]

print(sum(X) / len(X))