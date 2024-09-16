# 10수를 입력받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성

a = []
for _ in range(10):
    b = int(input("숫자를 입력해주세요"))
    a.append(b)
c = max(a)
print(f'가장 큰 숫자는 {c} 입니다.')



# map을 이용한 코딩

# map_list = list(map(int, input().split()))
# print(map_list)
# print(max(map_list))