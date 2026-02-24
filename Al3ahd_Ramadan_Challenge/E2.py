a = int(input())

DEGREE_PER_HOUR = 360 / 12
DEGREE_PER_MINUTE = 360 / 60

found = False
degree_hours = 0
degree_minutes = 0
match = [0, 0]
for hour in range(12, 21):
  for minute in range(0, 60):
    if abs(degree_hours - degree_minutes) == a:
      match = [hour, minute]
      found = True
      break
    degree_minutes += DEGREE_PER_MINUTE
  if found:
    break
  degree_hours += DEGREE_PER_HOUR
  degree_minutes = 0

print('{:02d}:{:02d}'.format(match[0], match[1]))
  