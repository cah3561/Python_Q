from tkinter import *

class cal_program:
    def __init__(self, window):
        self.window = window
        window.title("cal_program")  # 프로그램 이름 설정
        window.geometry("242x300")  # 크기 설정

        cc = Label(window, text="CALCULATOR", font=("Arial", 12))  # "CALCULATOR" 표기
        cc.grid(row=0, column=0, columnspan=4, pady=5)  # 위치 조정

        self.display = Entry(window, font=("Arial", 10))  # 입력을 받을 창 생성 및 폰트 설정
        self.display.grid(row=1, column=0, columnspan=4, ipadx=50, ipady=5)  # 입력 창 위치와 크기 설정

        # 숫자 및 연산자 버튼 만들고, 각각의 위치와 동작 커맨드 설정
        # 버튼 스타일 변경을 위해 bg(배경색), fg(글자색) 추가
        button_texts = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3)
        ]

        for text, row, col in button_texts:
            button = Button(window, text=text, command=self.push_bt(text),
                            bg="lightblue", fg="black", font=("Arial", 10))
            button.grid(row=row, column=col, padx=2, pady=2, ipadx=10, ipady=10)
    def push_bt(self, 입력변수):
        def f_push():
            if 입력변수 == '=':  # =을 눌렀을 때
                try:
                    입력된것 = self.display.get()  # 현재 입력창에 입력된 것 가져오기
                    결과 = eval(입력된것)  # 문자열로 가져온 '입력된것'을 eval()함수를 이용하여 결과 도출 
                    self.display.delete(0, 'end')  # 입력창 초기화
                    self.display.insert('end', 결과)  # 결과를 출력
                    self.is_result_shown = True  # 결과가 표시되었음을 표시
                except:  # 오류 처리
                    self.display.delete(0, 'end')  # 입력창 초기화
                    self.display.insert('end', "Error")  # 오류 메시지 출력
                    self.is_result_shown = False
            else:  # 숫자나 연산자가 입력된 경우
                if self.is_result_shown:  # 결과가 표시된 상태에서 새로운 입력이 들어오면
                    if 입력변수 in '0123456789':  # 새로운 입력이 숫자인 경우
                        self.display.delete(0, 'end')  # 입력창을 초기화하고
                        self.is_result_shown = False
                    else:  # 새로운 입력이 연산자인 경우
                        self.is_result_shown = False
                        # 결과 표시 상태를 유지하고, 연산자를 입력창에 추가하지 않습니다.
                        # 이 부분을 수정하여, 결과에 연산자를 추가하는 로직을 구현할 수 있습니다.
                self.display.insert('end', 입력변수)  # 입력된 문자를 창에 추가하여 출력
        return f_push  # 각 입력변수에 따른 적절한 함수를 반환

if __name__ == "__main__":  # 코드 실행
    window = Tk()
    app = cal_program(window)
    window.mainloop()