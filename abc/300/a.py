input_list = list(map(int, input().split()))
input_list_answer = list(map(int, input().split()))

result = input_list[1] + input_list[2]

for i in range(len(input_list_answer)):
          if input_list_answer[i] == result:
                    print(i + 1)
                    break