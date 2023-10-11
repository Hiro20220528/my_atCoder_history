N = input() 
S = input() 

hash_func = {}
hash_func['|'] = 0
hash_func['*'] = 0
hash_func['.'] = 0

def check(S):
          for chr in S:
                    hash_func[chr] += 1
                    if hash_func['|'] == 1 and hash_func['*'] == 1:
                              return True
                    if hash_func['|'] == 0 and hash_func['*'] == 1:
                              return False
                    if hash_func['|'] == 2:
                              return False
                              
if check(S):
          print("in")
else:
          print("out")