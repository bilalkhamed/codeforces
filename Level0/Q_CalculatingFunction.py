n = int(input())

# total = 0
# for i in range(1, n+1):
#   if i % 2 == 0:
#     total += i
#   else:
#     total += -1 * i
# print(total)

print(sum(i if i % 2 == 0 else i*-1 for i in range(1, n+1)))