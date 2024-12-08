# 실패 코드 1 -> ())(() 통과 못함
# def solution(s):
#     answer_left = 0
#     answer_right = 0
#     if s[0] == ")" or s[-1] == "(":
#             return False
#     for i in s:
#         if i == "(":
#             answer_left += 1
#         else:
#             answer_right += 1
#     if answer_left != answer_right:
#         return False
#     return True

def solution(s):
    answer = 0
    for i in s:
        if i == "(":
            answer += 1
        else:
            answer -= 1
        if answer < 0:
            return False
    if answer > 0:
        return False
    return True