N = int(input())

A = list(map(int, input().split()))

A.sort(reverse=True)

max_num = A[0]

for i in A:
    if max_num != i:
        print(i)
        break