def solution(s):
    answer = list(s)
    count = int(len(answer) / 2)

    if len(answer) % 2 != 0:
        return answer[count]
    else:
        return answer[count-1]+answer[count]
