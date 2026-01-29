n = int(input())

if n % 2 == 0:
  print(n//2)
else:
  rounded_up = (n+2-1) // 2
  print(int(rounded_up * -1))