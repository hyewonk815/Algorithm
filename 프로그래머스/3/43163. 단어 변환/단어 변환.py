from collections import deque

def solution(begin, target, words):
    queue = deque([(begin, 0)]) # 시작 노드와 변환 횟수를 큐에 삽입 / 튜플로 묶어주기
    
    if target not in words:
        return 0
    
    while queue:
        now_word, step = queue.popleft()
        
        if now_word == target:
            return step
        
        for word in words:
            count = 0
            for i in range(len(begin)):
                if word[i] != now_word[i]:
                    count += 1
            if count == 1:
                queue.append((word, step + 1))
    return 0