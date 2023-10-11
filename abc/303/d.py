# aのキー, shif+aのキー, CapsLockのキー
X, Y, Z = map(int, input ().split())

# 文字列S
S = input() 

hash = {}
hash['a'] = 0
hash['A'] = 0
for i in range(len(S)):
          hash[S[i]] += 1


print(hash)