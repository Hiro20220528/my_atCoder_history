H, W = map(int, input ().split())
A = [input().split() for _ in range(H)]
B = [input().split() for _ in range(H)]
          
aadot = [char[0].count('#') for char in A]

bbdot = [char[0].count('#') for char in B]

adot = {}
for i in range(len(A)):
          k = 0
          for chr in A[i][0]:
                    if chr == '#':
                              kchr = (k, chr)
                              adot[kchr] = adot.get(kchr, 0) + 1
                    k += 1
                    
bdot = {}
for i in range(len(B)):
          k = 0
          for chr in B[i][0]:
                    if chr == '#':
                              kchr = (k, chr)
                              bdot[kchr] = bdot.get(kchr, 0) + 1
                    k += 1

avalue = [value for value in adot.values()]

bvalue = [value for value in bdot.values()]

if sum(avalue) == H and A != B:
          print('No')
elif set(avalue) == set(bvalue) and set(aadot) == set(bbdot):
          print('Yes')
else:
          print('No')
          
# if adot == bdot:
#           print('Yes')
# else:
#           print('No')
