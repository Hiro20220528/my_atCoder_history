S = input() 

# ACE、BDF、CEG、DFA、EGB、FAC、GBD のいずれかと等しいとき Yes
mozi = {}
mozi['ACE'] = True
mozi['BDF'] = True
mozi['CEG'] = True
mozi['DFA'] = True
mozi['EGB'] = True
mozi['FAC'] = True
mozi['GBD'] = True


if mozi.get(S, False):
          print("Yes")
else:
          print("No")