def solution(participant, completion):
  answer = ''
  participant.sort()
  completion.sort()
  for x in range(len(completion)):
    if participant[x] != completion[x]:
      answer = participant[x]
    else:
      answer = participant[-1]
  return answer


