a, b, c = map(int, input().split())

if a+b>c and a+c>b and b+c>a:
  print(0)
else:
  ls = sorted([a, b, c])
  flag = 0
  while not (ls[0]+ls[1]>ls[2] and ls[0]+ls[2]>ls[1] and ls[1]+ls[2]>ls[0]):
    if flag % 2 == 0:
      ls[0] += 1
    else:
      ls[1] += 1
    flag += 1
  print(flag)