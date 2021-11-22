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

#대화창
ent = Entry(root)
ent.config(width= 10)
ent.get()
ent.pack()

def ent_p():
    a = ent.get()
    print(a)

btn1 = Button(root)
btn1.config(text= "확인")
btn1.config(command= ent_p)
btn1.pack()

btn2 = Button(root)
btn2.config(text= "출력")
btn2.pack()

root.mainloop()