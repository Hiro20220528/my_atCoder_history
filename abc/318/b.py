N = int(input())

tile = [list(map(int, input().split())) for _ in range(N)]

max_graph = 100

graph = [[0]*max_graph for _ in range(max_graph)]
# print(tile)

max_x = 0
max_y = 0
for row in tile:
          left_x = row[0]
          right_x = row[1]
          down_y = row[2]
          up_y = row[3]
          
          max_x = max(max_x, right_x)
          max_y = max(max_y, up_y)
          
          for i in graph[down_y:up_y]:
                    i[left_x:right_x] = [1 for _ in range(right_x-left_x)]
                    
                    
# print(graph)
total = 0
for i in graph[:max_y]:
          total += sum(i[:max_x])
                    
print(total)
