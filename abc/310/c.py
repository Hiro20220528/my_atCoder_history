N = int(input())

A = {input().split()[0]:True for _ in range(N)}

# hash = {}
# A = [input().split() for _ in range(N)]
# for chr in A:
#           chr = chr[0]
#           hash[chr] = hash.get(chr, 0) + 1

# # print(A)
# same = 0
# for key in hash.keys():
#           if hash.get(key, False):
#                     same += 1
#                     print(key, hash.get(key, False))
#           elif hash.get(key[::-1], False):
#                   same += 1
#                   print(key, hash.get(key[::-1], False))
          
# print(len(A) - same)

same = 0
for key in A.keys():
          if key == key[::-1]:
                    continue
          # print(key)
          if A.get(key[::-1], False):
                    # print(A.get(key[::-1], False))
                    same += 1
                    A[key] = False

# print(A, same)
# print(len(A))
print(len(A) - same)