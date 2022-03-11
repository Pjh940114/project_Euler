# 17
# 1부터 5까지의 수를 영어로 쓰면 one, two, three, four, five 이고,
# 각 단어의 길이를 더하면 3 + 3 + 5 + 4 + 4 = 19 이므로 사용된 글자는 모두 19개입니다.

# 1부터 1,000까지 영어로 썼을 때는 모두 몇 개의 글자를 사용해야 할까요?

# 참고: 빈 칸이나 하이픈('-')은 셈에서 제외하며, 단어 사이의 and 는 셈에 넣습니다.
#   예를 들어 342를 영어로 쓰면 three hundred and forty-two 가 되어서 23 글자,
#   115 = one hundred and fifteen 의 경우에는 20 글자가 됩니다.

import re
 
lines = []

# 파일을 불러와서 가공
with open('1_to_1000_in_english.txt', 'r') as file:
    for line in file:
        res = []
        p = re.compile("[^0-9]")
        res =''.join(line.split())
        lines.append(''.join(p.findall(res)))
 
# 가공된 파일 저장
with open('final.txt', 'w') as file:
    file.write('\n'.join(lines))

# "-" 제거
with open('final.txt', 'r') as file:
    for line in file:
        res = []
        p = re.compile("[^-]")
        res = ''.join(line.split())
        lines.append(''.join(p.findall(res)))

# 글자 수 저장
count = 0
for line in lines:
    count += len(line)

# and 갯수 : 100 ~ 1000, 99 * 9 * 3
count_and = 99 * 9 * 3

print("total count :", count + count_and)