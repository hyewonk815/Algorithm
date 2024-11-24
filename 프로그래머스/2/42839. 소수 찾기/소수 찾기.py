from itertools import permutations
import math

def solution(numbers):
    answer = 0
    number_list = list(numbers)
    set1 = set()
    for i in range(1, len(number_list)+1):
        result = permutations(number_list, i)
        for r in result:
            set1.add(int("".join(r)))
    for num in set1:
        if num < 2:
            answer += 0
            continue
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1 # 소수임
    return answer