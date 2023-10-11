A = list(map(int, input().split()))

result = 0
for i, number in enumerate(A):
    result += number * 2 **i
    
print(result)