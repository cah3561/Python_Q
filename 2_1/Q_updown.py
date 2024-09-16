# 랜덤 숫자 맞추기
from random import*
from tkinter import*

an = randint(1,100)

def make():
    t = Entry.get()
    print("맞춰보시오.", t)
def guess():
    global an
    g = int(e1.get())
    if g > an :
        l2.config(text="DOWN")
    elif g < an:
        l2.config(text="UP")
    elif g == an:
        l2.config(text="BINGO!")
    else:
        l2.config(text="무언가 잘못됐어요.")

def reset():
    global an
    e1.delete(0,END)
    an =randint(1,100)
    l2.config(text="")



p = Tk()

#제목 만들기
l1 = Label(p,text = "UP_DOWN")
l1.grid(row=0, column=0)
l2 = Label(p,text="")
l2.grid(row=3, column=0)

#빈칸 하나 만들기
e1 = Entry(p)
e1.grid(row=1, column=0)

# 버튼 2개 만들기
b1 = Button(p)
b1.grid(row=2,column=0,text="guess",COMMAND=guess)
b2 = Button(p)
b2.grid(row=2, column=1,text="reset",COMMAND=reset)


# p_1 = Tk.entry(p)
# p_1.pack()