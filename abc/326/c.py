N, M = map(int, input().split())

A = list(map(int, input().split()))
A.sort()
A.append(10**9)
# 尺取法を使用する
ans = 0
r = 0
for l in range(N):
    left = A[l] - 0.5
    xM = left + M
    
    right = A[r]
    while right < xM and r < N:
        r += 1
        # print(r)
        right = A[r]
        
    ans = max(ans, r - l)
print(ans)

# 二分探索を使用すると時間計算量がnlognで TLEになった

# # ハッシュに保存する
# index_hash = {}
# for k, num in enumerate(A):
#     index_hash[num] = k
    
# # print(index_hash)

# def binary_search(array, target):
#     # print(array, target)
#     if len(array) == 1:
#         return array[0]
#     middle = len(array) // 2
#     if array[middle] >= target:
#         ans = binary_search(array[:middle], target)
#     else:
#         ans = binary_search(array[middle:], target)
    
#     return ans

# max_count = 0
# history = {}
# for i in range(N):
#     x = A[i] - 0.5
#     if x in history:
#         continue
    
#     history[x] = True
#     xM = x + M
#     tmp_count = 0
#     index = binary_search(A, xM)
#     index = index_hash[index]
#     tmp_count = index - i + 1
#     max_count = max(max_count, tmp_count)
    
# print(max_count)


    