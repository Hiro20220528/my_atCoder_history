N, M = map(int, input().split())

A = list(map(int, input().split()))

winner = float('inf')
winner_vote = 0

candidate_list = [0 for _ in range(N)]

for vote in A:
    vote -= 1
    candidate_list[vote] += 1
    if candidate_list[vote] > winner_vote:
        winner_vote = candidate_list[vote]
        winner = vote
    elif candidate_list[vote] == winner_vote:
        if winner > vote:
            winner = vote
        
    print(winner+1)