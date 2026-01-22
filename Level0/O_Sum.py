t = int(input())

for i in range(t):
  a = list(map(int, input().split()))
  if a[0] + a[1] == a[2] or a[0] + a[2] == a[1] or a[1] + a[2] == a[0]:
    print('yes')
  else:
    print('no') 

