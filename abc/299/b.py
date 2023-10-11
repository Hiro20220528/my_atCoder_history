N, T = map(int, input ().split())

color = list(map(int, input().split()))
value = list(map(int, input().split()))

# card color
# card value

if T not in color:
          T = color[0]
          
initial_value = -1
for i in range(N):
          if color[i] == T and value[i] > initial_value:
                    winner = i + 1
                    initial_value = value[i]
print(winner)
                    
