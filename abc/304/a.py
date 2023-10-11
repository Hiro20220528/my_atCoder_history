N = int(input())

people = A = [input().split() for _ in range(N)]


people = [list(a)[::-1] for a in zip(*people)]


age = [int(char) for char in people[1]]
people[0].reverse()
age.reverse()

# print(people)
index = age.index(min(age))
# print(index)
order = people[0][index:] + people[0][:index]

# order.reverse()

for name in order:
          print(name)
