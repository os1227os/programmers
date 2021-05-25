def solution(a,b):

  days = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
  date = [31,29,31,30,31,30,31,31,30,31,30,31]

    
  return days[(sum(date[:a-1]) + b) % 7]
