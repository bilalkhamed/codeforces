l1, r1, l2, r2 = map(int, input().split())

if l2 > r1 or l1 > r2:
  print('-1')
elif (l1 > l2 and r1 > r2) or (l2 > l1 and r2 > r1):
  print('here')
  print(max(l1, l2), min(r1, r2))
else:
  if r1 > l2:
    print(l2, r1)
  else:
    print(r1, l2)


# Inside: (1, 10) U (3, 6) = 

# (2, 8) U (6, 10)

# (6, 10) U (2, 8)

# No intersection: (2, 8) U (9, 10)
