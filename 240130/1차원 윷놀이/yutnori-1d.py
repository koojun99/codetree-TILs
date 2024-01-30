def max_score(n, m, k, moves):
    def backtrack(turn, scores, positions):
        nonlocal max_score
        if turn == n:
            max_score = max(max_score, sum(scores))
            return
        
        for i in range(k):
            current_position = positions[i]
            new_position = current_position + moves[turn]
            
            if new_position <= m:
                positions[i] = new_position
                if new_position == m:
                    scores[i] += 1
                backtrack(turn + 1, scores, positions)
                if new_position == m:
                    scores[i] -= 1
                positions[i] = current_position
    
    max_score = 0
    positions = [0] * k
    backtrack(0, [0] * k, positions)
    return max_score

# 입력 처리
n, m, k = map(int, input().split())
moves = list(map(int, input().split()))

result = max_score(n, m, k, moves)
print(result)