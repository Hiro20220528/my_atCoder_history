N = int(input())

if N <= 10**3 -1:
          print(N)
elif N <= 10**4 - 1 and N >= 10**3:
          print(N // 10 * 10)
elif N <= 10**5 - 1 and N >= 10**4:
          print(N // 10**2 * 10 **2)
elif N <= 10**6 - 1 and N >= 10**5:
          print(N // 10**3 * 10 **3)
elif N <= 10**7 - 1 and N >= 10**6:
          print(N // 10**4 * 10 **4)
elif N <= 10**8 - 1 and N >= 10**7:
          print(N // 10**5 * 10 **5)
          # print("8")
elif N <= 10**9 - 1 and N >= 10**8:
          print(N // 10**6 * 10 **6)