from operator import itemgetter, attrgetter
from fractions import Fraction
N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]

people = [0] * N
for i, result in enumerate(A):
          rate = float(Fraction(result[0]) / Fraction(sum(result)))
          people[i] = rate, i+1
          
sort = sorted(people, key = itemgetter(0), reverse=True)

kekka = [0] * N
for i, person in enumerate(sort):
          kekka[i] = person[1]
          
print(*kekka)

