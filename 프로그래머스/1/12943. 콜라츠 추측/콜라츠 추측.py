def solution(num):
    count = 0
    number = num
    if num == 1:
        count += 0
    else:
        while number:
            if number == 1:
                break
            if count > 500:
                count = -1
                break
            else:
                if number % 2 == 0:
                    count += 1
                    number = number / 2
                else:
                    count += 1
                    number = (number * 3) + 1
    return count