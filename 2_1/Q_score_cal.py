

# 학생 수 결정
student_num = int(input("학생 수를 입력해주세요."))

# 학생 성적 변수 선언
student_score ={}
student_total={}
# 등급 배열 선언
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-','D0']

# 학생 정보 및 성적 입력
for i in range(student_num):
    name = str(input("이름을 입력해주세요."))
    middle = int(input("중간 고사 점수: "))
    final = int(input("기말 고사 시험: "))
    report = int(input("과제 점수: "))
    student_score[name]  = {'middle': middle, 'final': final, 'report': report}
    total_score = ((middle*0.4) + (final*0.4) + (report*0.2))
    student_total[name] = {'total': total_score, 'grade':None}

# 점수 합계 오름차순으로 정렬
sorted_total = sorted(student_total.items(), key=lambda x: x[1]['total'])
total = {key: value for key, value in sorted_total}


# 인원수에 맞게 구간 배정할 인원수 설정
part = int(student_num // 10) 

# 학생 등급 배분
# 10명 미만일 경우 모두 A+
b=0
if part == 0:
    for i in total:
        total[i]['grade'] = grade[0]
# 10명 이상일 경우 구간을 나워서 배분
else: 
    # 학생 수에서 구간을 나눈 만큼 반복
    for j in range(student_num // part +1):
        #각 구간에 할당된 인원 만큼 반복해서 등급을 부여해준다. 
        for k in range(part*j, part* (j+1)):
            # 마지막에 10개의 등급에 할당 받지 못한 인원이 있을경우 멈춘다.
            if j >= len(grade):
                b=j
                break
            total[k]['grade']= grade[j]
# 할당 받지 못한 인원에게 D0로 통일해서 준다.
    for y in range(student_num % 10,0,-1):
        total[b-y] = grade[-1]


    
print(f'학생 성적표>> {total}')

