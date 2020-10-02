from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
#import speech_recognition as s

engine=pp.init()

rate = engine.getProperty('rate')   
print (rate)                        
engine.setProperty('rate',100)



voice=engine.getProperty('voices')
print(voice)

engine.setProperty('voice',voice[1].id)

def speak(word):
  engine.say(word)
  engine.runAndWait()


bot = ChatBot("Alko")

convo = [
  "Hey",
  "Hi",
  "Hello",
  "How are you?",
  "Doing great these days,but bored",
  "How’s it going",
  "Good"
  "How are you doing",
  "Great",
  "Help",
  "Are you real?",
  "No,I am virtual",
  "Are you human or bot?",
  "Tell me a joke",
  "My New Years resolution is 1080p"
  "I love you",
  "Bye",
  "Thanks",
  "Yes I am bot,but :) one",
  "How old are you?"
  "I was created on 28/may/2020",
  "Tell me something ?",
  "Something :)",
  "what is your name?",
  "I name is ALKO",
  "Who created you",
  "Some you konw ",
  "Good Morning",
  "oday was not like yesterday and will never be like tomorrow. So always live life to the fullest and make the most of everything! Good morning",
  "Good Evening",
  "If you can look at the sunset and simle,then you still have hope",
  "Good Night",
  "I can’t wait to see your beautiful face tomorrow, but in the meantime, goodnight and sweet dreams",
  "Are you smart",
  "No,but smart then you",
  "Will you marry me",
  "You’re cute",
  "How are you",
  "I am doing great these day,but bored",
  "In which city you live",
  "I live in Karwar",
  "Which other language you know",
  "I know only english",
  "Bye",
  "Bye:( :( see you again"
]


trainer=ListTrainer(bot)

trainer.train(convo)


#to get response

#ans=bot.get_response("How are you")
#print("Talk t bot")


main=Tk()

main.geometry("500x600")

img=PhotoImage(file="botpic.png")

piclabel=Label(main,image=img)
piclabel.pack()

###take audio input from user
##def take_query():
##  sr=s.Recognizer()
##  sr.pause_threshold=1
##  print("bot is listing")
##  with s.Microphone() as m:
##    audio =sr.listen(m)
##    query=sr.recognize_google(audio,language="eng-in")
##    print(query)
##    textF.delete(0,END)
##    textF.insert(0,query)
##    ask_from_bot()





  


def ask_from_bot():
        query=textf.get()
        ans_bot = bot.get_response(query)#ans is in statement from
        msg.insert(END,"You : "+ query)
        msg.insert(END,"Bot : " +str(ans_bot))
        speak(ans_bot)
        textf.delete(0,END)
        msg.yview(END)#in scroll window upwards 



frame=Frame(main)

sc=Scrollbar(frame)
msg=Listbox(frame,width=80,height=20,yscrollcommand=sc.set)
#yscrollcommand=sc.set this active the scroll



sc.pack(side=RIGHT,fill=Y)
msg.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()

#textfeld
textf=Entry(main,font=("Verdana",20))
textf.pack(fill=X,pady=10)


#to create button
btn=Button(main,text="Ask from Bot",font=("verdana",20),command=ask_from_bot)
btn.pack()


# creating function
def enter_function(event):
        btn.invoke()


#binding main window with enetr
main.bind("<Return>",enter_function)



#takequery()

main.mainloop()




















