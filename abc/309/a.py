A, B = map(int, input().split())

if B - A == 1:
          if A <= 3 and B <= 3:
                    print("Yes")
          elif A > 6 and B > 6:
                    if A <= 9 and B <= 9:
                              print("Yes")
                    else:
                              print("No")
          elif A > 3 and B > 3:
                    if A <= 6 and B <= 6:
                              print("Yes")
                    else:
                              print("No")
          
          else:
                    print("No")
          
else:
          print("No")