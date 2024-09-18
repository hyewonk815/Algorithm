def solution(a, b):
    answer = ''
    now_day = b
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    for i in range(a-1):
        now_day += day[i]
    answer = week[(now_day%7) - 1]
    return answer