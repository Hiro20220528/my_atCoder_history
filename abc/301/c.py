import sys

S = input() 
T = input()


snum = {}
tnum = {}
for i in range(len(S)):
          schar = S[i]
          tchar = T[i]
          
          snum[schar] = snum.get(schar, 0) + 1
          tnum[tchar] = tnum.get(tchar, 0) + 1
          
atmark = ['a', 't', 'c', 'o', 'd', 'e', 'r']
   
sdiff = snum.items() - tnum.items()       
tdiff = tnum.items() - snum.items()  
  
# print(sdiff, tdiff)

for taple in sdiff:
          moji = taple[0]
          if moji != '@' and moji not in atmark:
                    # print(moji)
                    print("No")
                    sys.exit()
          elif moji != '@':
                    wild = tnum.get('@', 0)
                    while  snum.get(moji, 0) - tnum.get(moji, 0) > 0:
                              # print('wild', wild)
                              if wild == 0:
                                        print("No")
                                        sys.exit()
                              tnum[moji] = tnum.get(moji, 0) + 1
                              wild-=1
                              tnum['@'] = tnum.get('@', 0) - 1
                              
                    wild = snum.get('@', 0)
                    while  tnum.get(moji, 0) - snum.get(moji, 0) > 0:
                              # print('wild', wild)
                              if wild == 0:
                                        print("No")
                                        sys.exit()
                              snum[moji] = snum.get(moji, 0) + 1
                              wild-=1
                              snum['@'] = snum.get('@', 0) - 1
                              
for taple in tdiff:
          moji = taple[0]
          if moji != '@' and moji not in atmark:
                    # print(moji)
                    print("No")
                    sys.exit()
          elif moji != '@':
                    wild = snum.get('@', 0)
                    while  tnum.get(moji, 0) - snum.get(moji, 0) > 0:
                              # print('wild', wild)
                              if wild == 0:
                                        print("No")
                                        sys.exit()
                              snum[moji] = snum.get(moji, 0) + 1
                              wild-=1
                              snum['@'] = snum.get('@', 0) - 1
                              
                    wild = tnum.get('@', 0)
                    while  snum.get(moji, 0) - tnum.get(moji, 0) > 0:
                              # print('wild', wild)
                              if wild == 0:
                                        print("No")
                                        sys.exit()
                              tnum[moji] = tnum.get(moji, 0) + 1
                              wild-=1
                              tnum['@'] = tnum.get('@', 0) - 1
                              
# snum['@'] = 0
# tnum['@'] = 0
          
# print(sdiff, tdiff)
# print(snum, tnum)

if snum == tnum:
          print("Yes")
else:
          print("No")