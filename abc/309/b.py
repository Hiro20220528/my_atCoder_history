N = int(input())

A = [input().split() for _ in range(N)]

B = [['0'* N] for _ in range(N)]

print(A)

ac = [list(a)[::-1] for a in zip(*A)]
print(ac)

print("------")
print(B)

