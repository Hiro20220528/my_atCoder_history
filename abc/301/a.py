N = int(input())
S = input() 


result = {}
for winner in S:
          result[winner] = result.get(winner, 0) + 1


reverse_player = {}
reverse_player["T"] = "A"
reverse_player["A"] = "T"
if result.get("T", 0) == result.get("A", 0):
          print(reverse_player[winner])
             
elif result.get("T", 0) > result.get("A", 0):
          print("T")
else:
          print("A")