N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]

seat_z = sum(z[2] for z in A)

for i in A:
          x = i[0]
          y = i[1]
          z = i[2]
          if x - y > 0:
                    print(z)

print(seat_z // 2 + 1)