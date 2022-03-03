# 수 145는 신기한 성질이 있습니다. 각 자릿수의 팩토리얼(계승)을 더하면  1! + 4! + 5! = 1 + 24 + 120 = 145 처럼 자기 자신이 됩니다.

# 이렇게 각 자릿수의 팩토리얼을 더하면 자기 자신이 되는 모든 수의 합을 구하세요.

# 단, 1! = 1 과 2! = 2 의 경우는 덧셈이 아니므로 제외합니다.

import math
total = 0
limit = math.factorial(9) # 범위 지정

for i in range(3,limit+1):
    factorial_num = str(i)

    sum = 0
    for j in factorial_num:
        sum += math.factorial(int(j))

    if i == sum:
        print(i)
        total += i

print("total:",total)
    