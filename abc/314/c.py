N, M = map(int, input().split())

S = list(input())

C = list(map(int, input().split()))

color_hash = {}
for index, (text, color) in enumerate(zip(S, C)):
          # print(index, text, color)
          
          if color_hash.get(color, False):
                    color_hash[color] += text
          else:
                    color_hash[color] = text
          
for hash_key in color_hash.keys():
          moji = color_hash[hash_key]
          color_hash[hash_key] = moji[-1] + moji
          

history = {}
result = ''
for color in C:
          index =  history.get(color, 0)
          result += color_hash[color][index]
          history[color] = history.get(color, 0) + 1

# print(color_hash)
print(result)
          
          