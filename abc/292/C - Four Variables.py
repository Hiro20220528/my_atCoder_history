N = int(input())
# Nは正の整数
def countDivisor(num_map):
          count = 0
          length = (len(num_map) // 2) + 1
          # print(num_map)
          # print(length)
          num = 0
          for n_map in num_map:
                    left = 1
                    right = 1
                    for i in range(1, n_map[0]):
                          if n_map[0] % i == 0:
                              #       print(n_map[0], i, 'i')
                                    left+=1  
                    for i in range(1, n_map[1]):
                          if n_map[1] % i == 0:
                              #       print(n_map[1], i, 'i')
                                    right+=1 
                    
                    num += 1
                    wa = left * right
                    if length == num:
                              if length % 2 == 2:
                                        wa = wa * 2
                              count = count * 2
                              count += wa
                              return count
                    count += wa
                    # print(count, 'count') 
                    
          return count

def getAdd(N):
          answer = [((i+1), N - (i+1)) for i in range((N // 2) - 1)]
          return answer
          
          

print(countDivisor(getAdd(N)))     