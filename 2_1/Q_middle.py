# 중간값 구하기
# 입력으로 n 개의 숫자가 주어졌을 때, 중간 값을 찾아라
# 홀수인 n을 입력받는다
# 9~199 사이의 랜덤한 정수 n 개를 생성한다.
# 정수 n개의 중간 값을 출력한다.

import random

l =[]

a = int(input("홀수인 정수 생성 개수를 입력해주세요."))
for i in range(a):
    k = random.randint(9,199)
    l.append(k)
l.sort()
b = a // 2
print(f'배열의 나열: {l}')
print(f'배열의 중간값은 {l[b]}')