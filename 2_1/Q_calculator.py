from tkinter import *

class cal_program:
    def __init__(self, window):
        self.window = window
        window.title("cal_program")  # 프로그램 이름 설정
        window.geometry("350x430")  # 크기 설정

        cc = Label(window, text ="CALCULATOR", font =("TK Gothic", 15))  # "My Circulator" 표기
        cc.grid(row = 0, column = 0, columnspan = 4, pady = 20)  # 위치 조정
        # row(행) column(열) columnspan(열 위치) pady(y 방향 외부 패딩)

        self.display = Entry(window)  # 입력을 받을 창 생성
        self.display.grid(row =1, column = 0, columnspan = 4, ipadx= 100, ipady = 20)  # 입력 창 위치와 크기 설정
        # row(행) column(열) columnspan(열 위치) ipadx(x 방향 내부 패딩) ipady(y 방향 내부 패딩)


        # 숫자 및 연산자 버튼 만들고, 각각의 위치와 동작 커맨드 설정
        a1 = Button(window, text = '7', command = self.push_bt('7'))
        a1.grid(row = 2, column = 0, padx = 5, pady = 5, ipadx = 20, ipady = 20)
        
        # row(행) column(열) padx(x 방향 외부 패딩) pady(y 방향 외부 패딩)
        a2 = Button(window, text = '8', command = self.push_bt('8'))
        a2.grid(row = 2, column = 1, padx = 5, pady = 5, ipadx = 20, ipady = 20)
        a3 = Button(window, text = '9', command = self.push_bt('9'))
        a3.grid(row = 2, column = 2, padx = 5, pady = 5, ipadx = 20, ipady = 20)
        a4 = Button(window, text = '/', command = self.push_bt('/'))
        a4.grid(row = 2, column = 3, padx = 5, pady = 5, ipadx = 20, ipady = 20)
        
        b1 = Button(window, text = '4', command = self.push_bt('4'))
        b1.grid(row = 3, column = 0, padx = 5, pady = 5, ipadx = 20, ipady = 20)
        b2 = Button(window, text = '5', command = self.push_bt('5'))
        b2.grid(row = 3, column = 1, padx = 5, pady = 5, ipadx = 20, ipady = 20)
        b3 = Button(window, text = '6', command = self.push_bt('6'))
        b3.grid(row = 3, column = 2, padx = 5, pady = 5, ipadx = 20, ipady = 20)
        b4 = Button(window, text = '*', command = self.push_bt('*'))
        b4.grid(row = 3, column = 3, padx = 5, pady = 5, ipadx = 20, ipady = 20)
        
        c1 = Button(window, text = '1', command = self.push_bt('1'))
        c1.grid(row = 4, column = 0, padx = 5, pady = 5, ipadx = 20, ipady = 20)
        c2 = Button(window, text = '2', command = self.push_bt('2'))
        c2.grid(row = 4, column = 1, padx = 5, pady = 5, ipadx = 20, ipady = 20)
        c3 = Button(window, text = '3', command = self.push_bt('3'))
        c3.grid(row = 4, column = 2, padx = 5, pady = 5, ipadx = 20, ipady = 20)
        c4 = Button(window, text = '-', command = self.push_bt('-'))
        c4.grid(row = 4, column = 3, padx = 5, pady = 5, ipadx = 20, ipady = 20)
        
        d1 = Button(window, text = '0', command = self.push_bt('0'))
        d1.grid(row = 5, column = 0, padx = 5, pady = 5, ipadx = 20, ipady = 20)
        d2 = Button(window, text = '.', command = self.push_bt('.'))
        d2.grid(row = 5, column = 1, padx = 5, pady = 5, ipadx = 20, ipady = 20)
        d3 = Button(window, text = '=', command = self.push_bt('='))
        d3.grid(row = 5, column = 2, padx = 5, pady = 5, ipadx = 20, ipady = 20)
        d4 = Button(window, text = '+', command = self.push_bt('+'))
        d4.grid(row = 5, column = 3, padx = 5, pady = 5, ipadx = 20, ipady = 20)

    def push_bt(self, 입력변수):
        def  f_push(): 
# 버튼이 눌렸을 때 작동하도록 하는 클로저 
# 이 내부 함수없이 작동시키면 '789/456*123-0.=212.82236842105266+'라는 출력값이 나오는데
# 이는 버튼 생성시 바로 함수를 불러서 결과를 출력하여 발생하는 오류
            if 입력변수 == '=':  # =을 눌렀을 때
                try:
                    입력된것 = self.display.get()  # 현재 입력창에 입력된 것 가져오기
                    결과 = eval(입력된것)  # 문자열로 가져온 '입력된것'을 eval()함수를 이용하여 결과 도출 
                    self.display.insert(END, f"={결과}")  # 입력했던 수식과 결과를 출력
                except:  # 오류 처리
                    self.display.delete(0, END)  # 입력창 초기화
                    self.display.insert(END, "")  # 계산 불가능 시 공백 표기(초기화처럼 이용 가능)
            else:  # 숫자나 연산자가 입력된 경우
                self.display.insert(END, 입력변수)  # 입력된 문자를 창에 추가하여 출력
        return  f_push  # 각 입력변수에 따른 적절한 함수를 반환

if __name__ == "__main__": # 코드 실행
    window = Tk()
    app = cal_program(window)
    window.mainloop()

# 되도록 lambda를 사용하지 않는 방식으로 작성
# lambda를 사용하여 버튼 할당을 한다면 클로저를 사용할 필요도, 버튼 할당이 길어질 이유도 없음
# lambda를 사용하려면 위 코드의 19번째부터 71번째 줄을 아래 코드로 수정하면 됨

    #     buttons = [
    #         ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    #         ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    #         ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    #         ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
    #     ]
    # # 버튼에 표시될 문자, 행과 열 위치를 각각 입력하여 buttons로 선언


    #     for (text, row, column) in buttons:
    #         button = Button(window, text=text, command=lambda t=text: self.push_bt(t))
    #         button.grid(row=row, column=column, padx=5, pady=5, ipadx=20, ipady=20)
    # # 각 버튼을 반복문을 돌려서 표시될 문구를 넣어주고 lambda를 활용하여 각각의 버튼이 눌렸을 때 어떤 함수 결과를 얻을지 연결

    # # 아래 코드는 클로저가 없는 것을 제외하면 위와 같음
    # def push_bt(self, 입력변수):
    #     if 입력변수 == '=':
    #         try:
    #             입력된것 = self.display.get()
    #             결과 = eval(입력된것)
    #             self.display.insert(END, f"={결과}")
    #         except:
    #             self.display.delete(0, END)
    #             self.display.insert(END, "")

    #     else:
    #         self.display.insert(END, 입력변수)
