from collections import deque

def solution(cacheSize, cities):
    answer = 0
    lru = deque()
    for i in cities:
        i = i.lower()
        if i in lru:
            answer += 1
            lru.remove(i)
            lru.append(i)
        else:
            answer += 5
            lru.append(i)
            if len(lru) > cacheSize:
                lru.popleft()
    return answer