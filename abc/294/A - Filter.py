N = int(input())

A = list(map(int, input().split()))

odd = [i  for i in A if i % 2 == 0]

for out in odd:
          print(out,end=' ')