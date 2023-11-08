# 二部グラフの計算量はo(V+E)

# 再帰の回数を撤回する
import sys
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

graph = {}

# 隣接リストを作成する
for i,j in zip(A, B):
    if i in graph:
        graph[i].append(j)
    else:
        graph[i] = [j]
        
    if j in graph:
        graph[j].append(i)
    else:
        graph[j] = [i]
        
# print(graph)

# visited = set()
flag = True
def dfs(v, number):
    if v < 0 or v > n:
        return
    # print('============================')
    global flag
    
    
    # print(visited)
    # print(number_list)
    # print(flag)
    
    if number_list[v-1] is None:
        number_list[v-1] = number
    elif number_list[v-1] != number:
        # print(number_list[v-1], number)
        flag = False
        
    if v in visited or flag == False:
        return
    # print(f"v: {v} -> number: {number}")
    visited.add(v)
        
    if v in graph:
        for next_node in graph[v]:
            if v == next_node:
                flag = False
                return
            dfs(next_node, number^1)
    return
   
number_list = [None for _ in range(n)] 
visited = set()
for v in range(n):
    
    # print(f'node v: {v+1} -> 1')
    num = number_list[v]
    if num is None:
        dfs(v+1, 1)
if flag:
    print("Yes")
else:
    print('No')