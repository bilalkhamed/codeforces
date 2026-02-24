# Runtime Error on test 3

angles = {
  0: 3,
  30: 4,
  60: 5,
  90: 6,
  120: 7,
  150: 8,
  180: 9,
  210: 10,
  240: 11,
  270: 12,
  300: 1,
  330: 2
}



a = int(input())

ls = list(angles.keys())
match = None
for i in range(len(ls)):
  for k in range(i, len(angles.values())):
    if (abs(ls[k] - ls[i]) == a):
      # print(ls[k], ls[i])
      match = (i, k)
      break
  if not match is None:
    break

first = ls[match[0]]
second = ls[match[1]]

hours = angles[first] + 12 if angles[first] < 12 else angles[first]
minutes = angles[second] * 5


# print(angles[first], angles[second])

print(f'{hours}:{str(minutes).zfill(2)}')
