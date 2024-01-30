def max_score(n, m, k, moves):
    def backtrack(turn, scores, position):
        nonlocal max_score
        if turn == n:
            max_score = max(max_score, max(scores))
            return
        
        for i in range(k):
            current_position = position[i]
            new_position = current_position + moves[turn]
            
            if new_position <= m:
                position[i] = new_position
                scores[i] += 1
                backtrack(turn + 1, scores, position)
                position[i] = current_position
                scores[i] -= 1
    
    max_score = 0
    position = [1] * k  # 각 말의 시작점을 1로 초기화
    backtrack(0, [0] * k, position)
    return max_score

# 입력 처리
n, m, k = map(int, input().split())
moves = list(map(int, input().split()))

result = max_score(n, m, k, moves)
print(result)