# 학점 계산기
# 총 10개의 평점이 존재 A+~D0
# 총점 = 중간 (35) + 기말 (45) + 과제 (20)
# 10개의 평점을 총점이 높은 순으로 부여
# 각각의 평점은 같은 비율로 부여
# 입력: 학생 수 / 각 학생의 과제 점수
# 학점을 알고 싶은 학생 k 가 주어졌을 때, k 번째 학생의 학점을 출력
studen_l ={}
info =[]
num_student = int(input("학생 수를 입력해주세요."))

def input_d():
    
    for i in range(num_student):
        name = input('이름을 입력해주세요.')
        middle = int(input('중간 점수를 입력해주세요.'))
        final = int(input("기말 점수를 입력해주세요."))
        report = int(input("과제 점수를 입력하세요."))
        score_s = {'name':name,'middle':middle,'final':final, 'report':report}
        info.append(score_s)
    return info

studen_l = input_d()

def cal(info):
    total_s =[]
    for j in info:
        total = j['middle'] * 0.35 
        + j['final'] * 0.45 + j['report'] * 0.2
        total_s.append(total)
    return total_s


total_score = cal(studen_l)

# for k in studen_l:
print(total_score)

