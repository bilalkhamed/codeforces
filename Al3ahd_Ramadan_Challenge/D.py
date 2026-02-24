n = int(input())

dishes = {input() for _ in range(n)}

for dish in sorted(dishes, reverse=False):
  print(dish)
