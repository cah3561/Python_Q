# 삼각형 만들기
# 크기가 N인 삼각형을 만들자.
# 첫 줄은 항상 1이다.
# 그 다음 줄을 만들 때 바로 위의 왼쪽 숫자와 오른쪽 숫자를 더한다.

a = int(input("N을 입력해주세요."))
c =[]

for i in range(a):
    b=[]
    for j in range(i+1):
        if j == 0 or j == i:
            b.append(1)
        else:
            b.append(c[i-1][j] +c[i-1][j-1])
    c.append(b)
for i in c:
    print(*i)