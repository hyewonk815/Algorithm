def solution(seoul):
    answer = ""
    if "Kim" in seoul:
        answer = str(seoul.index("Kim"))
    return "김서방은 " + answer + "에 있다"