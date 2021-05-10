def solution(nums):
    n=len(nums)//2   # 고를수 있는 갯수 
    find=list(set(nums))   #  고를수 있는 종류
    return min(n,find)

