N, M = map(int, input().split())

fire_work_days = list(map(int, input().split()))

queue_index = 0

all_days = [i+1 for i in range(N)]

for day in all_days:
          next_fire_work_day = fire_work_days[queue_index]
          
          ans = next_fire_work_day - day
          
          if ans == 0:
                    queue_index += 1
          print(ans)

