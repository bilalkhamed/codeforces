a, b, c = map(int, input().split())

ls = sorted([a, b, c])
if ls[0] + ls[1] > ls[2]:
  print(0)
else:
  print(ls[2] - (ls[0] + ls[1]) + 1)