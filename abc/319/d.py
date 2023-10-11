N, M = map(int, input().split())

A = list(map(int, input().split()))

a = sum(A)

# print(a + N)
max_A = a + N

array = [i for i in range(max_A + 1)]

def binary_search(max_A, array, M, A, N):
          left = 0
          right = max_A - 1
          
          while right - left > 1:
                    m = left + (right - left) // 2
                    # k文字でM行に収まるか
                    k = array[m]
                    
                    index = 0
                    loop_count = 0
                    for i in range(M):
                              r = 0
                              while index < N and r + A[index] <= k:
                                        r += A[index]
                                        if r != k:
                                                  r += 1
                                        index += 1
                              
                    if index < N:
                              left = m
                    else:
                              right = m                    
                    # print('')
                    # print(k, 'moji', left, right, index, N)
                    # index = 0
                    # flag = True
                    # loop_count = 0
                    # for row in range(M):
                    #           loop_count = row + 1
                    #           if index > N:
                    #                     flag = False
                    #                     break
                    #           r = 0
                    #           while True:
                    #                     print(r, end=' ')
                    #                     if index >= N:
                    #                               print("-")
                    #                               break
                    #                     if r + A[index] <= k:
                    #                               # print(r, end=' ')
                    #                               r += A[index]
                    #                     else:
                    #                               if loop_count == M:
                    #                                         flag = False
                    #                               else:
                    #                                         index += 1
                    #                               print("--", r)
                                                  
                    #                               break
                                        
                    #                     if r == k:
                    #                               if loop_count == M and index < N:
                    #                                         flag = False
                    #                               else:
                    #                                         index += 1
                    #                               print("----", k, r, index, N)
                                                  
                    #                               break
                    #                     else:
                    #                               r += 1
                    #                     index += 1
                        
                    # print('')                
                    # print(loop_count, M, index, flag)
                    # # if loop_count != M:
                    # if loop_count != M or flag == False:
                    #           print('no')
                    #           left = m 
                    # else:
                    #           print('ok')
                    #           right = m 
                              
          return right         
                                                  
print(binary_search(max_A, array, M, A, N))