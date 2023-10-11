N, D = map(int, input().split())

# S = [list(input().split()) for _ in range(N)]
S = [input().split() for _ in range(N)]

A = [0 for _ in range(N)]
for i, chr in enumerate(S):
          A[i] = list(chr[0])

# print(A)

A = [list(a)[::-1] for a in zip(*A)]

# print(A)

count = 0
sum_list = []
for each in A:
          if ''.join(each) == 'o'*N:
                    count += 1
          else:
                    sum_list.append(count)
                    count = 0
sum_list.append(count)
print(max(sum_list))