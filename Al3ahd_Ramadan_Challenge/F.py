# AC, 93 ms - 4900 KB

n = int(input())

dishes = list(map(int, input().split()))

dishes.sort()

max_cals = int(input())


current_cals = 0
total_dishes = 0
for dish in dishes:
  if current_cals > max_cals:
    break
  elif current_cals + dish <= max_cals:
    current_cals += dish
    total_dishes += 1

print(total_dishes, max_cals - current_cals)