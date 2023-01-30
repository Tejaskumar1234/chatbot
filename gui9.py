
from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot=ChatBot('Bot')
trainer=ListTrainer(bot)
data=open('medico12.yaml', 'r', encoding='utf-8').readlines()
chatbot = ChatBot("...")
chatbot.storage.drop()

trainer.train(data)

def send():
    question = questionField.get()
    answer = bot.get_response(question)
    textarea.insert(END, 'I:  ' + question + '\n\n')
    textarea.insert(END, 'MEDICO:  ' + str(answer) + '\n\n')
    questionField.delete(0, END)
def Close():
    root.destroy()

def open_win():
    new = Toplevel(root)
    new.geometry("500x570")
    new.config(bg='skyblue')
    new.title("MANUAL WINDOW")
        # Create a Label in New window
    Label(new, text="MANUAL", font=('Arial,14,bold')).pack(side=TOP)
    tc=Label(new,text="MEDICO\nWhat is medico ??\nMedico is an AI text based chat bot developed using python.\nIt can clear the doubts of auser about the covid-19 and also \nit can detect the name of the disease along withprecautionary measures to take\nHow you can use it\nI. Type your symptoms\nType the symptoms name like fever, muscles pain , headache etc.\n Medico will giveappropriate responses to the input that is given by the user.\nSpecificationsOh! If I get a cold then it must be covid!!!▪\nDuring these days if one gets affected by cold \nit may be due to the cold environment orthe exposure to corona virus medico will differentiate whether\nit is covid or not.\nItGoals\n1.To give a user an interactive experience about his/her health condition.\n2.To avoid scheduling with doctors during pandemics like covid-19\nMedical chatbots are AI-powered conversational solutions that help patients\n insurance companies, and healthcare providers easily connect with each other\nThese bots can also play a critical role in making relevant\nhealthcare information accessible to the right stakeholders\nThis chatbot provides the best possible precautionary measures\nbased on the input by the users for all acute diseaseandCOVID-19\n.",font=('Times new roman',10)).place(x=0,y=50)





    def Close2():
        new.destroy()
    bt2 = Button(new, text='back',command=Close2)
    bt2.config(bg='cyan4')
    bt2.pack()
    bt2.place(x=250,y=500)
    bt2.config(bg='honeydew')

def open_win2():
    new2 = Toplevel(root)
    new2.geometry("500x570")
    new2.config(bg='green')
    new2.title("ABOUT WINDOW")
        # Create a Label in New window
    Label(new2, text="ABOUT", font=('Arial,14,bold')).pack(side=TOP)
    lc=Label(new2,text="\nA Chabot is artificial intelligence (AI)\ncomputer software that can simulate a conversation using textual or audio techniques.\nIt helps to complete digital learning contentand\nwith the right AI-technology they can find new content that is relevant to the specificlearner\nMedical chatbots are AI-powered conversational solutions that help patients\n insurance companies, and healthcare providers easily connect with each other\nThese bots can also play a critical role in making relevant\nhealthcare information accessible to the right stakeholders\nThis chatbot provides the best possible precautionary measures\nbased on the input by the users for all acute diseaseandCOVID-19\n.",font=('Times new roman',10)).place(x=0,y=50)

    def Close3():
        new2.destroy()
    bt3 = Button(new2, text='back',command=Close3)
    bt3.config(bg='cyan4')
    bt3.pack()
    bt3.place(x=250,y=500)

def open():
    t= Toplevel(root)
    t.geometry("500x570")
    t.config(bg='cadet blue')
    t.title("help")
    Label(t,text="Help",font=('Arial',14)).pack(side=TOP)
    l=Label(t,text="\nCentral Helpline Number for corona-virus: - +91-11-23978046\nvisit this page for more info\nhttps://www.mygov.in/covid-19\nNational Coronavirus Helpline For information about COVID-19 and\nvaccines call1800 020 080.This line operates 24 hours a day,7 days a\nweek with additional options for prioritygroups\n",font=("Times new roman",12)).place(x=0,y=50)

    def C():
        t.destroy()
    Button(t,text='back',command=C).pack(side=BOTTOM)

root=Tk()


root.title("medical chatbot")
root.config(bg='lavender')
root.geometry('500x570+25+75')
label=Label(root,text="Say 'HI' to start!")
label.pack()
label1=Label(root,text="THE MEDICAL CHATBOT-'MEDICO'!")
label1.pack()
label1.place(x=150,y=105,width=200,height=30)
label.place(x=160,y=180,width=150,height=20)
label.config(bg='honeydew')
logoPic=PhotoImage(file='green-cross-medical-symbol-vector-20783578.png')
logoPicLabel=Label(root,image=logoPic)
logoPicLabel.pack()
logoPicLabel.place(x=180,y=0,height=100,width=100)
about=Button(root,text='about',command=open_win2)
about.grid(row=0,column=0)
about.place(x=0,y=0)
about.config(bg='green')
home=Button(root,text='help',command=open)
home.grid(row=1,column=0)
home.place(x=50,y=0)
home.config(bg='purple')
manual=Button(root,text='manual',command=open_win)
manual.grid(row=2,column=0)
manual.place(x=450,y=0)
manual.config(bg='sky blue')
questionField=Entry(root,width=40,font=('Arial',14))
questionField.config(bg='skyblue')
questionField.pack_configure(fill=Y)
questionField.place(x=0,y=150)

center=Frame(root)
center.pack()
center.place(x=0,y=200,width=500,height=300)
scrollbar=Scrollbar(center)
scrollbar.pack(side=RIGHT)
textarea=Text(center,font=('Arial',10),yscrollcommand=scrollbar.set,wrap='word')
textarea.pack()
scrollbar.config(command=textarea.yview)
send=Button(root,text='Send',command=send)
send.config(bg='grey')
send.place(x=450,y=150,width=50,height=25)
ex=Button(root,text="Exit",command=Close)
ex.pack()
ex.place(x=200,y=525,width=50,height=25)
ex.config(bg='red')




root.mainloop()
