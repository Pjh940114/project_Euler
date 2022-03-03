# 1
# 10보다 작은 자연수 중에서 3 또는 5의 배수는 3, 5, 6, 9 이고, 이것을 모두 더하면 23입니다.
# 1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?

sum = 0
numbers = range(1,1000)
for num in numbers:
    if num % 3 == 0 or num % 5 ==0:
        sum += num

print(sum)