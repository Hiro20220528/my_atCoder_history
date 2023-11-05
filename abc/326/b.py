N = int(input())

for number in range(N, 920):
    hyaku = number // 100
    ju = (number % 100) // 10
    ichi = ( (number % 100) % 10)
    
    if hyaku * ju == ichi:
        print(number)
        break