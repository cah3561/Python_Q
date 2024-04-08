# 369 시뮬레이션 결과를 출력
# 3,6,9는 X 로 출력한다.
# 박수를 두번 쳐야하는 경우는 XX로 출력

n = int(input("숫자를 입력해주세요."))

for i in range(1, n+1):
    n = str(i)
    c = 0
    c = n.count('3') + n.count('6') + c.count('9')

    if c > 0:
        print("x" * c, end=" ")
    else: 
        print(n, end='')