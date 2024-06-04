def solution(votes, k):
    winners = 0
    max_votes = max(votes)
    count = votes.count(max(votes))
    for i in range(len(votes)):
        if votes[i] + k > max_votes:
            winners += 1
        elif votes[i] == max_votes and count == 1:
            winners += 1
    return winners
