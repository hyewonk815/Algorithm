def solution(phone_number):
    count = len(phone_number[:-4])
    answer = phone_number.replace(phone_number[:-4], "*"*count)
    return answer