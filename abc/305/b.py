A = input().split()

A.sort()
q = A[1]
p = A[0]

line = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

value = [3, 1, 4, 1, 5, 9]

start = line.index(p)
end = line.index(q)

num = 0
for i in range(start, end):
          num += value[i]
print(num)
# print(p, q)
