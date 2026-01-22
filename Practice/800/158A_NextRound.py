n, k = map(int, input().split())

a = list(map(int, input().split()))

score = a[k-1]

passed = 0
for i in range(0, n):
  if a[i] > 0 and a[i] >= score:
    passed += 1

print(passed)