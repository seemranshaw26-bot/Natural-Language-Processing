from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import MyAPI
class NLP:
    def __init__(self):
       self.db=Database()
       self.apio = MyAPI()
        #login GUI
       self.root = Tk() #creating GUI
       self.root.title("NLP app")
       self.root.iconbitmap("resources/favicon.ico")
       self.root.geometry("350x600")
       self.root.configure(bg="white")
       self.login_GUI()
       self.root.mainloop() #it will hold the GUI
    def login_GUI(self):
        self.clear()
        LABEL= Label(self.root, text="NLP APP",bg="white",fg="blue")#making GUI login
        LABEL.pack(pady=(30,30))#giving GUI the space showing whats wriitten in LABEL
        LABEL.configure(font=("verdana",24,"bold"))

        label1= Label(self.root, text="Username",bg="white",fg="blue")
        label1.pack(pady=(10,10))
        self.username_input=Entry(self.root,width=50)
        self.username_input.pack(pady=(5,10),ipady=3)

        label2= Label(self.root, text="Email", bg="white", fg="blue")
        label2.pack(pady=(10,10))
        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=3)#ipady means increasing the height of the box

        label3 = Label(self.root, text="Password", bg="white", fg="blue")
        label3.pack(pady=(10, 10))
        self.password_input = Entry(self.root, width=50,show="*")
        self.password_input.pack(pady=(5, 10), ipady=3)

        login_button=Button(self.root, text="Login", bg="white", fg="blue",width=30,height=3,command = self.perform_login)#we cant give height in entry box but in button box
        login_button.pack(pady=(5, 10), ipady=3)

        label4 = Label(self.root, text="Not a member?", bg="white", fg="blue")
        label4.pack(pady=(20, 10))
        Redirect_button = Button(self.root, text="Register Now", bg="white", fg="blue",command=self.register_GUI)
        Redirect_button.pack(pady=(5, 10), ipady=3)

    def register_GUI(self):
        #clear the existing GUI
       self.clear()
       LABEL = Label(self.root, text="NLP APP", bg="white", fg="blue")  # making GUI login
       LABEL.pack(pady=(30, 30))  # giving GUI the space showing whats wriitten in LABEL
       LABEL.configure(font=("verdana", 24, "bold"))

       label1 = Label(self.root, text="Enter your username", bg="white", fg="blue")
       label1.pack(pady=(10, 10))
       self.name_input = Entry(self.root, width=50)
       self.name_input.pack(pady=(5, 10), ipady=3)

       label2 = Label(self.root, text="Enter your email", bg="white", fg="blue")
       label2.pack(pady=(10, 10))
       self.email_input = Entry(self.root, width=50)
       self.email_input.pack(pady=(5, 10), ipady=3)

       label3 = Label(self.root, text="Enter your password", bg="white", fg="blue")
       label3.pack(pady=(10, 10))

       self.password_input = Entry(self.root, width=50, show="*")
       self.password_input.pack(pady=(5, 10), ipady=3)

       password_info = Label(self.root, text="Password must contain 8 characters,\ncontains uppercase,lowercase and number", bg="white", fg="blue")
       password_info.pack(pady=(5, 10), ipady=3)

       Registration_button = Button(self.root, text="Register", bg="white", fg="blue", width=30,height=3,command=self.perform_registration)
       Registration_button.pack(pady=(5, 10), ipady=3)


       label4 = Label(self.root, text="Already a member?", bg="white", fg="blue")
       label4.pack(pady=(20, 10))

       Redirect_button = Button(self.root, text="Login Now", bg="white", fg="blue", command=self.login_GUI)
       Redirect_button.pack(pady=(5, 10), ipady=3)

    def clear(self):
       for i in self.root.pack_slaves():
            i.destroy()
    def perform_registration(self):
        #fetch data from GUI
       name= self.name_input.get()
       email = self.email_input.get()
       password= self.password_input.get()

       if (len(password) < 8 or
         not any(ch.isalpha() for ch in password )or
         not any(ch.isupper() for ch in password) or
         not any(ch.isdigit() for ch in password) or
         not any(ch.islower() for ch in password) ):
           messagebox.showerror("Error","Please enter a valid password")
           return

       if not email.endswith("@gmail.com"):
           messagebox.showerror("Error","Please enter a valid email address")
           return
       response= self.db.add_data(name,email,password)

       if response:
           messagebox.showinfo('success',"Registration Successful. You Can Login Now")
           self.login_GUI()
       else:
           messagebox.showerror("Error","Registration Failed")
    def perform_login(self):
        username = self.username_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        if not email.endswith("@gmail.com"):
            messagebox.showerror("Error", "Please enter a valid email address")
            return

        response=  self.db.search(username,email,password)
        if response:
            messagebox.showinfo('success',"Login Successful. You Can Login Now")
            self.home_GUI()
        else:
            messagebox.showerror("Error","Incorrect email/password")
    def home_GUI(self):
        self.clear()#again a clear dashboard

        LABEL = Label(self.root, text="NLP APP", bg="white", fg="blue")
        LABEL.pack(pady=(30, 30))
        LABEL.configure(font=("verdana", 24, "bold"))

        sentiment_button = Button(self.root, text="Sentiment Analysis", bg="white", fg="blue", width=30, height=4,command=self.sentiment_GUI)
        sentiment_button.pack(pady=(10, 10))

        NER_button = Button(self.root, text="Named Entity Recognisation", bg="white", fg="blue", width=30, height=3,command=self.NER_GUI)
        NER_button.pack(pady=(10, 10))

        Emotion_button = Button(self.root, text="Emotion Prediction", bg="white", fg="blue", width=30,height=3,command=self.emotion_GUI)
        Emotion_button.pack(pady=(10, 10))

        Redirect_button = Button(self.root, text="Log Out", bg="white", fg="blue", command=self.login_GUI)
        Redirect_button.pack(pady=(5, 10), ipady=3)

    def sentiment_GUI(self):
        self.clear()

        LABEL = Label(self.root, text="NLP APP", bg="white", fg="blue")
        LABEL.pack(pady=(30, 30))
        LABEL.configure(font=("verdana", 24, "bold"))

        LABEL2 = Label(self.root, text="Sentiment Analysis", bg="white", fg="blue")
        LABEL2.pack(pady=(10, 20))
        LABEL2.configure(font=("verdana", 20))

        label1 = Label(self.root, text="Enter your text", bg="white", fg="blue")
        label1.pack(pady=(20, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=3)

        sentiment_button = Button(self.root, text="Analyse Sentiment", bg="white", fg="blue", width=30, height=3,command=self.do_sentiment_analysis)
        sentiment_button.pack(pady=(5, 10), ipady=3)

        self.sentiment_result= Label(self.root, text="", bg="white", fg="blue")
        self.sentiment_result.pack(pady=(20, 10))

        self.sentiment_result.configure(font=("verdana", 16))

        goback_button = Button(self.root, text="Go Back", bg="white", fg="blue", width=30, height=3,command=self.home_GUI)
        goback_button.pack(pady=(5, 10), ipady=3)

    def do_sentiment_analysis(self):
        text= self.sentiment_input.get()
        result=self.apio.sentiment_analysis(text)

        txt=""
        for i in (result): #then all the section looks more clear
            label=i.label
            score=round(i.score *100,2)
            txt=txt+f"{label}- {score}%\n"


        self.sentiment_result["text"]=txt
        self.sentiment_result.configure(font=("verdana", 16))



    def NER_GUI(self):
        self.clear()

        LABEL = Label(self.root, text="NLP APP", bg="white", fg="blue")
        LABEL.pack(pady=(30, 30))
        LABEL.configure(font=("verdana", 24, "bold"))

        LABEL2 = Label(self.root, text="Named Entity Recognisation", bg="white", fg="blue")
        LABEL2.pack(pady=(10, 20))
        LABEL2.configure(font=("verdana", 16))

        label1 = Label(self.root, text="Enter your text", bg="white", fg="blue")
        label1.pack(pady=(20, 10))

        self.NER_input = Entry(self.root, width=50)
        self.NER_input.pack(pady=(5, 10), ipady=3)

        NER_button = Button(self.root, text="Recognise", bg="white", fg="blue", width=30, height=3,command=self.do_recognisation)
        NER_button.pack(pady=(5, 10), ipady=3)

        self.NER_result = Label(self.root, text="", bg="white", fg="blue")
        self.NER_result.pack(pady=(20, 10))

        self.NER_result.configure(font=("verdana", 16))

        goback_button = Button(self.root, text="Go Back", bg="white", fg="blue", width=30, height=3, command=self.home_GUI)
        goback_button.pack(pady=(5, 10), ipady=3)

    def do_recognisation(self):
            text = self.NER_input.get()
            result = self.apio.NER(text)

            txt = ""
            for i in (result):
                word = i.word
                entity=i.entity_group
                score = round(i.score * 100, 2)
                txt = txt + f"{word}--->{entity} ({score})%\n"

            self.NER_result["text"] = txt
            self.NER_result.configure(font=("verdana", 16))

    def emotion_GUI(self):
            self.clear()

            LABEL = Label(self.root, text="NLP APP", bg="white", fg="blue")
            LABEL.pack(pady=(30, 30))
            LABEL.configure(font=("verdana", 24, "bold"))

            LABEL2 = Label(self.root, text="Emotional Prediction", bg="white", fg="blue")
            LABEL2.pack(pady=(10, 20))
            LABEL2.configure(font=("verdana", 20))

            label1 = Label(self.root, text="Enter your text", bg="white", fg="blue")
            label1.pack(pady=(20, 10))

            self.emotion_input = Entry(self.root, width=50)
            self.emotion_input.pack(pady=(5, 10), ipady=3)

            emotion_button = Button(self.root, text="Analyse Emotions", bg="white", fg="blue", width=30, height=3,command=self.do_emotion_prediction)
            emotion_button.pack(pady=(5, 10), ipady=3)

            self.emotion_result = Label(self.root, text="", bg="white", fg="blue")
            self.emotion_result.pack(pady=(20, 10))

            self.emotion_result.configure(font=("verdana", 16))

            goback_button = Button(self.root, text="Go Back", bg="white", fg="blue", width=30, height=3,command=self.home_GUI)
            goback_button.pack(pady=(5, 10), ipady=3)

    def do_emotion_prediction(self):
                text = self.emotion_input.get()
                result = self.apio.Emotion(text)

                txt = ""
                for i in (result):  # then all the section looks more clear
                    label = i.label
                    score = round(i.score * 100, 2)
                    txt = txt + f"{label}- {score}%\n"

                self.emotion_result["text"] = txt
                self.emotion_result.configure(font=("verdana", 16))



face=NLP()
