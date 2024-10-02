from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    peoples = deque(people)
    while peoples:
        person = peoples.pop()
        if len(peoples) > 0 and person + peoples[0] <= limit:
            peoples.remove(peoples[0])
        answer += 1
    return answer