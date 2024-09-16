# 자릿수 더하기

# 하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성
# 자연수 n을 입력 받는다.
# n의 각 자릿수의 합을 출력한다.

# n = int(input("숫자를 입력해주세요."))

# s = []

# while n>0:
#     s.append(n % 10)
#     n //= 10

# print(sum(s))

# map을 이용한 코딩

number = list(map(int, input()))
print(number)
print(sum(number))

# num, num2, num3 = map(int,int())
# print(num)
