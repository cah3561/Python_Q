# 홀수 계산하기 
# 0~100 까지 무작위 수 10개 주어짐
#       random 활용
#       10개의 숫자를 출력한다.
# 10개의 숫자 중 홀수인 수만 더한 값을 출력한다.

import random

i = [random.randint(0, 100) for _ in range(10)]
print("생성된 숫자: ", i)

sum_odd = sum(a for a in i if a % 2 !=0 )

print("추출된 숫자 중 홀수의 합: ", sum_odd)

