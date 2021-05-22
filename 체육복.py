def solution(n, lost, reserve):
    
    result_reserve = set(reserve) - set(lost)  # 집합을 이용하여 중복값 제거후 차집합
    result_lost = set(lost) - set(reserve)   
    
    for i in result_reserve: # 여분의 체육복이 있는 학생의 왼쪽부터 탐색
        if i-1 in lost: 
            result_lost.remove(i-1) # 왼쪽학생이 잃어버렸다면 도난 당한 학생 집합에서 제거 
        elif i+1 in reserve: # 왼쪽 학생이 안 잃어버렸다면 오른쪽학생탐색
            result_lost.remove(i+1)
            
    return n-len(result_lost)  # 전체 학생수에서 체육복 못빌린 학생 수만큼 뺸 값을 return 
