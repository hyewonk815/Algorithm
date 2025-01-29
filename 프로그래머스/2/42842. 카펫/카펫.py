# 조건 1 : h <= w 
# 조건 2 : brown+yellow = h * w
# 조건 3 : yellow = (h-2)(w-2)
# 조건 4 : brown = 2h + 2w - 4 => 2 * (h+w-2)
def solution(brown, yellow):
    total = brown + yellow
    for height in range(1, total):
        if total % height == 0 and height <= (total // height):
            width = total // height
            if brown == 2 * (height+width-2):
                return [width, height]