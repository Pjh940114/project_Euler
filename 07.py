# 7 
# 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.

# 이 때 10,001번째의 소수를 구하세요.

num = 1
i = 1

while (num <= 10002):
    i += 1
    result = True
    
    for j in range(2, i):
        if i % j == 0:
            result = False
            break
    
    if result == True:
        num += 1
    
    if num == 10002:
        print("10001번째 소수 : " , i)

