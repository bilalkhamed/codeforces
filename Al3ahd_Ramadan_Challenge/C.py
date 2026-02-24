# n = int(input())

# s = input()

# ls = list(s)

# count = {
#   's': 0,
#   'r': 0
# }

# for char in ls:
#   count[char] += 1

# print('Rawan' if count['r'] > count['s'] else 'Shatha')

import sys
# def determine_winner(s):
#     count_r= s.count("r")
#     count_s= s.count("s")

#     if count_r > count_s:
#         return "Rawan"
#     elif count_s > count_r:
#         return "Shatha"
#     else:
#         return "Draw"

# n = int(input())
# s= input()
 

# result= determine_winner(s)
# print(result)

import sys
def determine_winner(s):
    count_r= s.count("r")
    count_s= s.count("s")

    if count_r > count_s:
        return "Rawan"
    elif count_s > count_r:
        return "Shatha"
    else:
        return "Draw"

input_data= sys.stdin.read().split()
 
print(input_data)
if input_data:
    s= input_data[1]
    result= determine_winner(s)
    print(result)