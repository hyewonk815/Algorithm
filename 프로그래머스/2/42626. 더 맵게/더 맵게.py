import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) < 2 :
            return -1
        k1 = heapq.heappop(scoville)
        k2 = heapq.heappop(scoville)
        heapq.heappush(scoville, k1 + (k2*2))
        answer += 1
    return answer


## 실패 1 : 정렬 문제
# from collections import deque

# def solution(scoville, K):
#     answer = 0
#     scoville.sort()
#     scoville_deque = deque(scoville)
#     while scoville_deque[0] < K:
#         if len(scoville_deque) < 2:  # 음식이 2개 미만이면 불가능
#             return -1
#         k1 = scoville_deque.popleft()
#         k2 = scoville_deque.popleft()
#         scoville_deque.append(k1 + (k2*2))
#         answer += 1
#     return answer

## 실패 2 : 효율성 테스트 X
# def solution(scoville, K):
#     answer = 0
#     scoville.sort()
#     while scoville[0] < K:
#         if len(scoville) < 2:  # 음식이 2개 미만이면 불가능
#             return -1
#         k1 = scoville.pop(0)
#         k2 = scoville.pop(0)
#         scoville.append(k1 + (k2*2))
#         answer += 1
#         scoville.sort()
#     return answer

