N = int(input())

W = input().split()

def check_english(W):
          for chr in W:
                    if chr == 'and' or  chr == 'that' or  chr == 'not' or  chr == 'the' or  chr =='you':
                              return True
                    
          return False

if check_english(W):
          print('Yes')
else:
          print('No')