S = input()

mozi = ['a', 'e', 'i', 'o', 'u']

for m in mozi:
          S = [i for i in S if i != m]

          S = ''.join(S)

print(S)
