def cal_dist(i_arr):
    # 변수 선언 (초기속도&최종속도)
    start_sp = 0 
    end_sp = 0 
    # 입력 횟수 만큼 반복 실행
    for i in i_arr: 
        if i[0] == 0:  # 현재 속도 유지 명령
            pass
        elif i[0] == 1: # 가속 명령
            start_sp += i[1]
        elif i[0] == 2: # 감속 명령
            start_sp -= i[1]
            if start_sp < 0: # 현재 속도 보다 감속할 속도가 더 클 경우 0 만들기
                start_sp = 0
        end_sp += start_sp # 합산
    return end_sp # 최종 속도 리턴

# 명령 배열 선언
i_arr = [] 
# 반복횟수 받기
n = int(input("반복 횟수: ")) 
# N 만큼 반복
# 명령 내용 받기 -> 명령배열에 저장
for i in range(n):  
    i = list(map(int, input("명령 입력: ").split())) 
    i_arr.append(i) 

print("이동 거리:", cal_dist(i_arr)) 
