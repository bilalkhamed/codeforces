from math import log2

t = int(input())

for _ in range(t):
  n = int(input())

  total = (n*(n+1))//2

  powers_sum = 0
  i = 1
  while i <= n:
    powers_sum += i
    i *= 2

  print(int(total- (2 *powers_sum)))
