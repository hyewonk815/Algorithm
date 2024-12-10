def solution(numbers, k):
    answer = 0
    num = ((k-1) * 2) % len(numbers)
    answer += numbers[num]
    return answer