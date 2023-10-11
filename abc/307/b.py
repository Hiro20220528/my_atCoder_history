import sys
N = int(input())

A = [input().split() for _ in range(N)]

# 全探索
for i in range(len(A)):
          s1 = A[i][0]
          for k in range(i + 1, len(A)):
                    # print(i, k)
                    s2 = A[k][0]
                    kaibun1 = s1 + s2
                    kaibun2 = s2 + s1
                    # print(kaibun1, kaibun2)
                    if kaibun1 == kaibun1[::-1] or kaibun2 == kaibun2[::-1]:
                              print("Yes")
                              sys.exit()
                    
print("No")
                    
                    