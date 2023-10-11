N = int(input())
A = list(map(int, input().split()))


out = []
for i in range(len(A) - 1):
# for i in range(1):
          # print('i:', i)
          out.append(A[i])
          if abs(A[i] - A[i + 1]) != 1:
                    if A[i] > A[i + 1]:
                              # print(">")
                              tmp = A[i] - 1
                              while tmp > A[i + 1]:
                                        out.append(tmp)
                                        tmp -= 1
                                        # print(out)
                    else:
                              # print("<")
                              tmp = A[i] + 1
                              while A[i + 1] > tmp:
                                        out.append(tmp)
                                        tmp += 1
                                        # print(out)

out.append(A[-1])
print(*out)