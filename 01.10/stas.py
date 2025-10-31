import random

scores = [random.randint(50, 100) for _ in range(50)]

def check_winner(scores: list, student_score: int) -> str:
  scores.sort()
  if len(scores) <= 3:
    'стас молодец'
  return 'стас молодец' if student_score in scores[-3:] else 'стас не молодец'
