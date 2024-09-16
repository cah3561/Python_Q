import random
from tkinter import *

window = Tk()
window.geometry("500x300")
secret_number = random.randint(1, 100)
print(secret_number)
guess = None

def guess_number():
    global secret_number
    guess = int(entry.get())
    if guess == secret_number:
        message = "축하합니다!!"
    elif guess <  secret_number:
        message = "Low"
    else:
        message = "High!"
    result['text']= message

def reset():
    global secret_number
    entry.delete(0, END)
    secret_number = random.randint(1, 100)
    print(secret_number)
    message = "1부터 100사이의 숫자를 추측하시오"
    label['text']= message

message = "Guessing Game"
label = Label(window, text=message, font=("Arial", 20))
label.place(x=100, y=30)

entry = Entry(window, font=("Arial", 15))
entry.place(x=100, y=100)
guess_button = Button(window, text="guess", font=("Arial", 15), command=guess_number)
reset_button = Button(window, text="reset", font=("Arial", 15), command=reset)
guess_button.place(x=100, y=150)
reset_button.place(x=200, y=150)
result = Label(window, text="1부터 100 사이의 정수를 추측하세요", font=("Arial", 15))
result.place(x=100, y=200)


window.mainloop()