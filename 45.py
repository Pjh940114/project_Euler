# 45
# 삼각수, 오각수, 육각수는 아래 식으로 구할 수 있습니다.

# 삼각수	 	Tn = n (n + 1) / 2	 	1, 3, 6, 10, 15, ...
# 오각수	 	Pn = n (3n − 1) / 2	 	1, 5, 12, 22, 35, ...
# 육각수	 	Hn = n (2n − 1)	 	1, 6, 15, 28, 45, ...
# 여기서 T285 = P165 = H143 = 40755 가 됩니다.

# 오각수와 육각수도 되는, 그 다음으로 큰 삼각수를 구하세요.

from csv import list_dialects


list_t = []
list_p = []
list_h = []

for i in range(1,100000):
    list_t.append(i*(i+1)/2)
    list_p.append(i*(3*i-1)/2)
    list_h.append(i*(i*2-1))

# print(list_t, list_p, list_h)

for x in list_t:      
    if x in list_p and x in list_h:
        print(x)

