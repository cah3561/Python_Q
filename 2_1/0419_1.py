arr = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15]]

x, y = 0, 0

while True:
    direction = input("방향을 입력하세요 (오른쪽, 왼쪽, 위, 아래, 끝): ")
    
    if direction == "오른쪽":
        if y < len(arr[0]) - 1:  # 배열의 너비를 초과하지 않도록 검사
            y += 1
        else:
            print("더 이상 오른쪽으로 갈 수 없습니다.")
    elif direction == "왼쪽":
        if y > 0:
            y -= 1
        else:
            print("더 이상 왼쪽으로 갈 수 없습니다.")
    elif direction == "위":
        if x > 0:
            x -= 1
        else:
            print("더 이상 위로 갈 수 없습니다.")
    elif direction == "아래":
        if x < len(arr) - 1:  # 배열의 높이를 초과하지 않도록 검사
            x += 1
        else:
            print("더 이상 아래로 갈 수 없습니다.")
    elif direction == "끝":
        print("프로그램을 종료합니다.")
        break
    
    print(f"현재 위치의 값: {arr[x][y]}")
