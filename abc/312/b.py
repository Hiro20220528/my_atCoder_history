import os
N, M = map(int, input().split())

tak_code = [input() for _ in range(N)]

if N < 8 or M < 8:
          print("")
          os.exit()

# print(tak_code)

left_list = [
          '###.',
          '###.',
          '###.',
          '....'
]

right_list = [
          '....',
          '.###',
          '.###',
          '.###'
]
# debug
# print('debug')
# print(tak_code)
# print(tak_code[0][0:4])
# print(tak_code[0][5:9])
# print('-----')
zero = True
for i in range(N - 8):
          for j in range(M - 8):
                    initial = i
                    tail = i + 5
                    
                    flag = True
                    for k, answer in enumerate(zip(left_list, right_list)):
                              code_left = tak_code[initial + k][j:j+4]
                              code_right = tak_code[tail + k][j+5:j+9]
                              # print(code_right, code_left)
                              # print(answer[0], answer[1], answer, i, k)
                              if answer[0] != code_left or answer[1] != code_right:
                                        # print('break', code_left, code_right, answer[0], answer[1], i, k)
                                        flag = False
                                        break
                    if flag:
                              zero = False
                              print(i+ 1, j + 1)
          

# code_right_split = tak_code[:4]
# code_left_split = tak_code[-4:]
if zero:
          print('')
# print(code_right_split)
# print("-------------")
# print(code_left_split)