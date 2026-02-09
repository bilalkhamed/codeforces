# def is_prime(n):
#   if n < 2: return False
#   flag = True
#   for i in range(2, int(n ** 1/2)):
#     if n % i == 0:
#       flag = False
#       break
#   return flag


# for i in range(n+1):

n = int(input())
if n >= 13:
  print('YES')
else:
  print('NO')