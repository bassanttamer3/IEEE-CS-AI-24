if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))
    unique_scores = list(set(scores))
    max_score = max(unique_scores)
    unique_scores.remove(max_score)
    runner_up_score = max(unique_scores)

    print(runner_up_score)
