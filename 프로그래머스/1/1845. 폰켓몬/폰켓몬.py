def solution(nums):
    count = len(nums) / 2
    monster = len(set(nums))
    answer = min(count, monster)
    return answer