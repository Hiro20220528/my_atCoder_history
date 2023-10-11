N = int(input())

distance = N % 5

if distance > 2:
          print(N - distance + 5)
else:
          print(N - distance)