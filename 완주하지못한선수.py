def solution(participant, completion):

  participant.sort()
  completion.sort()

  for x in range(len(completion)):
    if participant[x] != completion[x]:
      return  participant[x]
  return  participant[-1]
  


