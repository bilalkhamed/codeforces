t = int(input())

for i in range(t):
  rating = int(input())

  match rating:
    case rating if rating >= 1900: 
      print('Division 1')
    case rating if rating >= 1600:
      print('Division 2')
    case rating if rating >= 1400:
      print('Division 3')
    case _:
      print('Division 4')