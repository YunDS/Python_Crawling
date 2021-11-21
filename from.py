#업로드 명령어 : 
# git pull -> 서버내용 로컬로 불러오기
# git add -> 가상영역에 로컬에서 적은 내용 업로드
# git status -> 가상영역에 올라간 내용 확인
# git commit -m "적고싶은 메시지" -> 커밋(로컬)
# git push -> 원격 저장소로 업로드



from tkinter import*

root = Tk()
count = 0
#라벨
root.title("동수 왔어요 뿌잉")
root.geometry("800x600+100+100")
root.resizable(False, False)

Label = Label(root, text="0")
Label.pack()


#버튼
# def countplus():
#     global count
#     count += 1
#     Label.config(text=str(count))

# def countminus():
#     global count
#     count -= 1
#     Label.config(text=str(count))

# button1 = Button(root, width=10, text="up", overrelief="solid", command=countplus)
# button1.pack()
# button2 = Button(root, width=10, text="down", overrelief="solid", command=countminus)
# button2.pack()
def buttonClicked():
    Label.configure(foreground='blue')
    LabelNew.configure(text=' ' + answer.get())

answer = root.StringVar()
textbox = Tk.Entry(root, width=12, textvariable=answer)
textbox.grid(column=0, row=1)

Label = Tk.Label(root, text="정답을 입력하세요")
Label.grid(column=0, row=0)

LabelNew = Tk.Label(root, text="")
LabelNew.grid(column=1, row=2)

button = Tk.Button(root, text="클릭", command=buttonClicked)
button.grid(column=1, row=1)

root.mainloop()