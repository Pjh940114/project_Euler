# 50
# 41은 소수이면서 다음과 같은 6개의 연속된 소수의 합으로도 나타낼 수 있습니다.

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# 이것은 100 이하에서는 가장 길게 연속된 소수의 합으로 이루어진 소수입니다.

# 1000 이하에서는 953이 연속된 소수 21개의 합으로 가장 깁니다.

# 1백만 이하에서는 어떤 소수가 가장 길게 연속되는 소수의 합으로 표현될 수 있습니까?
from sympy import isprime
    
max = 1000000

# 소수 리스트
primes = []
for n in range(2,max+1):
    if isprime(n):
        primes.append(n)

# 소수 합 리스트
prime_sum = [0]
sum = 0
count = 0
while sum < max:
  sum+=primes[count]
  prime_sum.append(sum)
  count+=1

print(prime_sum)

terms = 1 # 연속된 소수 개수
max_prime = 0 # 소수

for i in range(count):
  for j in range(i+terms, count):
    x = prime_sum[j] - prime_sum[i]

    if j-i > terms and isprime(x):
      terms, max_prime = j-i, x

print("max_prime = {}, terms = {}".format(max_prime, terms))



