N = int(input())
S = input() 

# 面接官の評価をハッシュ値に保存し条件を満たすか調べる
evaluation = {}
for value in S:
          evaluation[value] = evaluation.get(value, 0) + 1
if evaluation.get('o', 0) > 0 and evaluation.get('x', 0) == 0:
          print('Yes')
else:
          print('No') 
