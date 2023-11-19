N, Q = map(int, input().split())

S = input()

questions = [list(map(int, input().split())) for _ in range(Q)]

cumulative_sum = [0]

total = 0
for i in range(N-1):
    if S[i] == S[i+1]:
        total += 1
    cumulative_sum.append(total)
    
# print(cumulative_sum)

for q in questions:
    s = q[0]
    e = q[1]
    print(cumulative_sum[e-1] - cumulative_sum[s-1])