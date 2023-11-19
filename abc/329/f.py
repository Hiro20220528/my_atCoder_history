N, Q = map(int, input().split())
C = list(map(int, input().split()))

queries = [list(map(int, input().split())) for _ in range(Q)]

a = set()
boxes = [set() for _ in range(N)]

for i, ball in enumerate(C):
    boxes[i].add(ball)
    
for query in queries:
    f = query[0] - 1
    t = query[1] - 1
    boxes[t] = boxes[f].union(boxes[t])
    boxes[f].clear()
    print(len(boxes[t]))
    
        