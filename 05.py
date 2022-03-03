# 5
# 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.

# 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?

import math

lcm = 1

for i in range(1,21):
    gcd = math.gcd(lcm,i)
    lcm = int(lcm*i/gcd)
    print(i, lcm)