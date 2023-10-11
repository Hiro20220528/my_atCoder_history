N, Q = map(int, input ().split())

event_list = [list(map(int, input().split())) for _ in range(Q)]

player = [0 for _ in range(N)]
answer = []
for event in event_list:
          
          do = event[0]
          number = event[1] - 1
          if do == 1:
                    player[number] += 1
          elif do == 2:
                    player[number] += 2
          else:
                    if player[number] >= 2:
                              answer.append('Yes')
                    else:
                              answer.append('No')
[print(result) for result in answer]
