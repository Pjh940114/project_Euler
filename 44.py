# 44
# 오각수는 Pn = n (3n − 1)/2 라는 공식으로 구할 수 있고, 처음 10개의 오각수는 다음과 같습니다.

# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

# 위에서 P4 + P7 = 22 + 70 = 92 = P8이 됨을 볼 수 있습니다. 하지만 두 값의 차인 70 − 22 = 48 은 오각수가 아닙니다.

# 합과 차 모두 오각수인 두 오각수 Pj, Pk 에 대해서, 그 차이 D = | Pk − Pj | 는 가장 작을 때 얼마입니까?

from math import sqrt
# 오각수 판별 함수
def is_penta(n):
	return (1+sqrt(24*n+1))%6 == 0

def func():
	penta=lambda x: int(x*(3*x-1)/2)
	k=1
	while True:
		for i in range(1, 10000):
			if is_penta(penta(i+k)-penta(i)) and is_penta(penta(i+k)+penta(i)):
				return penta(i+k)-penta(i)
		k+=1
print(func())

