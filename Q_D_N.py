# n의 약수 구하기
# 1개의 정수를 입력 받아 이 정수의 약수를 오름차순으로 출력

k = []
a = int(input("정수를 입력해주세요."))
for i in range(1,a+1):
    if a % i == 0:
        k.append(i)

print(f' 약수는 {k}')
