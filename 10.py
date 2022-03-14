# 10
# 10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.

# 이백만(2,000,000) 이하 소수의 합은 얼마입니까?

from sympy import isprime
 
total = 0
i=1
while i < 2000000:
    if isprime(i):
        total += i
    i+=1
print(total)