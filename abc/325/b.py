N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]

# 各国の時間を基準とし1時間ごとに参加できる人数を数えて最大値を導く

time_diff = [0 for _ in range(N)]

for i in range(N):
    time_diff[i] = [(k+A[i][1]) % 24 for k in range(24)]


max_people = 0
for j in zip(*time_diff):
    tmp_people = 0
    for index, each_time in enumerate(j):
        if 9 <= each_time and each_time <= 17:
            tmp_people += A[index][0]
      
    max_people = max(max_people, tmp_people)
    
print(max_people)
            