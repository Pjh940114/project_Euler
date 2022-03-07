# 44
# 오각수는 Pn = n (3n − 1)/2 라는 공식으로 구할 수 있고, 처음 10개의 오각수는 다음과 같습니다.

# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

# 위에서 P4 + P7 = 22 + 70 = 92 = P8이 됨을 볼 수 있습니다. 하지만 두 값의 차인 70 − 22 = 48 은 오각수가 아닙니다.

# 합과 차 모두 오각수인 두 오각수 Pj, Pk 에 대해서, 그 차이 D = | Pk − Pj | 는 가장 작을 때 얼마입니까?

import math

penta_list = []
x = 2
while x < 5000:

    for n in range(1,x):
        penta_num = (n*(3*n-1)) / 2
        penta_list.append(penta_num)

    for i in range(x-1):
        for j in range(x-1):
            if i < j:
                penta_sum = penta_list[i] + penta_list[j]
                penta_sub = penta_list[i] - penta_list[j]

                if penta_sum in penta_list and penta_sub in penta_list:
                    print(abs(penta_sub))
                    break

        x += 1