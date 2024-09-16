from tkinter import*


# button = Button(window, text="클릭하세요.")
# button.pack()

# window.mainloop()

def cTof():
    e2.delete(0,END)
    c1 = float(e1.get())
    a = (c1 -32) * (5/9) 
    e2.insert(0,str(a))
    

def fToc():
    e1.delete(0,END)
    d1 = float(e2.get())
    b = (d1 *(9/5)) + 32
    e1.insert(0,str(b))
    
window = Tk()

l1 = Label(window, text="화씨")
l2 = Label(window, text="섭씨")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(window,text='화씨 -> 섭씨',command= cTof)
b2 = Button(window,text='섭씨 -> 화씨',command=  fToc)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)



    
window.mainloop()


