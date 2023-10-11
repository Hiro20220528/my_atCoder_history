N, M = map(int, input().split())

C = input().split()

D = input().split()

P = list(map(int, input().split()))

D = ["special"] + D

menu = {}
for d,p in zip(D, P):
          menu[d] = p
          
result = 0
for name in C:
          if menu.get(name, False):
                    result += menu[name]
          else:
                    result += menu["special"]
# print(menu)
print(result)
          
          