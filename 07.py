# 7 
# 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.

# 이 때 10,001번째의 소수를 구하세요.

from math import sqrt

prime_list = [2]
num = 3
while len(prime_list) < 10001:
    isPrime = True
    x = 0
    while prime_list[x] <= sqrt(num):
        if num % prime_list[x] == 0:
            isPrime = False
            break
        x += 1

    if isPrime:
        prime_list.append(num)
    num += 1
print("10001 번째 소수 :", max(prime_list))

