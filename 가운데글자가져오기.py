def solution(s):
    answer = list(s)
    count = int(len(answer) / 2)

    a = answer[count-1]
    b = answer[count]

    if len(answer) % 2 != 0:
        s = answer[count]
    else:
        s = a+b
    
    return s
