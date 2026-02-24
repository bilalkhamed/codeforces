d = int(input())
t = int(input())

extra_minutes = 40 + (t * (d-1))

if extra_minutes >= 60:
  extra_hours = 1
  minutes = extra_minutes - 60
  while minutes >= 60:
    minutes -= 60
    extra_hours += 1

  print(f'{6 + extra_hours}:{str(minutes).zfill(2)}')
else:
  print(f'6:{str(extra_minutes).zfill(2)}')