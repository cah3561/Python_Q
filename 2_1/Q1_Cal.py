import tkinter as tkt

window = tkt.Tk()
window.title("CALCULATOR") # 제목 

# 윈도우 크기 고정
window.resizable(0, 0)                               

# 변수 선언
entry = tkt.Entry(window) # 입력 빈칸
entry.grid(row=1, columnspan=8, padx=10, pady=10) # 빈칸 위치 선정

# 버튼 입력 함수
def button_p(num):
    current = entry.get() # 입력 값 가져오기
    entry.delete(0, tkt.END) # 초기화
    entry.insert(0, current + str(num)) # 합산
   
# 결과 값 도출 함수
def result():
    try:
        total = str(eval(entry.get())) # 계산해서 가져오기
        entry.delete(0, tkt.END) # 초기화
        entry.insert(0, total) # 삽입
    except Exception as e: # 에러처리
        entry.delete(0, tkt.END)
        entry.insert(0, "오류")
# 초기화 함수 
def C():
    entry.delete(0, tkt.END)
    
# 버튼 세팅 
Button0 = tkt.Button(window, text="0", bg='white',command=lambda: button_p(0), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button0.grid(row=6, column=2, padx=10, pady=10)
Button1 = tkt.Button(window, text="1", bg='white',command=lambda: button_p(1), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button1.grid(row=3, column=1, padx=10, pady=10)
Button2 = tkt.Button(window, text="2", bg='white',command=lambda: button_p(2), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button2.grid(row=3, column=2, padx=10, pady=10)
Button3 = tkt.Button(window, text="3", bg='white',command=lambda: button_p(3), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button3.grid(row=3, column=3, padx=10, pady=10)
Button4 = tkt.Button(window, text="4", bg='white',command=lambda: button_p(4), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button4.grid(row=4, column=1, padx=10, pady=10)
Button5 = tkt.Button(window, text="5", bg='white',command=lambda: button_p(5), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button5.grid(row=4, column=2, padx=10, pady=10)
Button6 = tkt.Button(window, text="6", bg='white',command=lambda: button_p(6), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button6.grid(row=4, column=3, padx=10, pady=10)
Button7 = tkt.Button(window, text="7", bg='white',command=lambda: button_p(7), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button7.grid(row=5, column=1, padx=10, pady=10)
Button8 = tkt.Button(window, text="8", bg='white',command=lambda: button_p(8), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button8.grid(row=5, column=2, padx=10, pady=10)
Button9 = tkt.Button(window, text="9", bg='white',command=lambda: button_p(9), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Button9.grid(row=5, column=3, padx=10, pady=10)
Plus = tkt.Button(window, text="+", bg='white',command=lambda: button_p("+"), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Plus.grid(row=3, column=4, padx=10, pady=10)
Minus = tkt.Button(window, text="-", bg='white',command=lambda: button_p("-"), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Minus.grid(row=4, column=4, padx=10, pady=10)
Multiply = tkt.Button(window, text="*", bg='white',command=lambda: button_p("*"), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Multiply.grid(row=5, column=4, padx=10, pady=10)
Divide = tkt.Button(window, text="/", bg='white',command=lambda: button_p("/"), height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Divide.grid(row=6, column=4, padx=10, pady=10)
Equal = tkt.Button(window, text="=", bg='white',command=result, height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Equal.grid(row=6, column=3, padx=10, pady=10)
Clear = tkt.Button(window, text="C", bg='white',command=C, height=1, width=7, borderwidth=1, relief=tkt.SOLID)
Clear.grid(row=6, column=1, padx=10, pady=10)

window.mainloop()