# Problem:
# Given scores of participants on Sports Day, find the runner-up score.
# Input:
#   - First line: integer n (number of scores)
#   - Second line: n space-separated integers (the scores)
# Output:
#   - Print the second highest (runner-up) score.

if __name__ == '__main__':
    n=int(input("Enter no. of scores: "))
    scores=list(map(int,input("Enter the scores: ").split()))

    winner=max(scores)

    filtered_scores=[x for x in scores if x!=winner]

    runner_up=max(filtered_scores)

    print(runner_up)

