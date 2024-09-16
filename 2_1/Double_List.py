# 이중리스트 실습


# n = int(input("크기를 입력해주세요."))
# a = [[0 for _ in range(n)] for _ in range(n)]
ex_list = [[1,2,3],
           [4,5,6],
           [7,8,9]]

current_row = 0
current_col =0
p = ex_list[0][0]
a= 0



while True:
    a = int(input("오른쪽: 0, 왼쪽: 1, 위: 2, 아래: 3, 끝: 6, 초기화: 4"))
    if a == 0: # 오른
        if current_col < len(ex_list[0])-1:
            current_col += 1
            p = ex_list[current_row][current_col]
            print(p)
        else:
            print("에러")
    elif a ==1: #왼
        if current_col > 0:
            current_col -= 1
            p = ex_list[current_row][current_col]
            print(p)
        else:
            print("에러")
    elif a == 2:#위
        if current_row > 0:
            current_row -= 1
            p = ex_list[current_row][current_col]
            print(p)
        else:
            print("에러")
    elif a==3: #아래
        if current_row < len(ex_list[0])-1:
            current_row += 1
            p = ex_list[current_row][current_col]
            print(p)
        else:
            print("에러")
    elif a==6:
        print("끝")
        break
    elif a ==4:
        current_row = 0
        current_col =0
        p = ex_list[0][0]

     







