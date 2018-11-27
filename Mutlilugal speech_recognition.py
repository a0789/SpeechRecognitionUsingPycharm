from tkinter import *
from  tkinter import filedialog
import speech_recognition as root
import tkinter as tk

window = Tk()
window.title("Speech_Recognition")
#window.configure(background='black')
#window.geometry('600*500')
l1=Label(window, text="Result")
l1.grid(row=1,column=3)
def record():
    capture=sr.Recognizer()
    with root.Microphone() as source:
        print("ready")
        audio=capture.listen(source)
        print("wait")

        with open('audio.wav','wb') as f:
            f.write(audio.get_wav_data())
            #print("done")
            text.insert(tk.INSERT,'Done')

b2=Button(window,text="Record",width=12,command=record)
b2.grid(row=5,column=2)

text=tk.Text(window,height=8,width=30)
text.grid(row=1,column=2)
text.config(state='normal')
def audiop():

    capture=root.Recognizer()
    audio=filedialog.askopenfilename(initialdir='/',title='Select A File',filetype=(('audio','*.wav'),("All Files",'*.*')))
    with root.AudioFile(audio) as source:
        text.insert(tk.INSERT,'audio picked\n')
        audio=capture.record(source)
        text.insert(tk.INSERT,'Please wait...\n')
        fron = capture.recognize_google(audio)
        fron1 = capture.recognize_google(audio,language='hi-IN')

    try:
       #fron = capture.recognize_google(audio)
       text.insert(tk.INSERT,fron )
       text.insert(tk.INSERT,fron1)
       #print(capture.recognize_google(audio))
       #print(capture.recognize_google(audio,language='hi-IN'))

    except:
       #print('error')
       text.insert(tk.INSERT,'Error')



b4=Button(window,text='Browse audio',width=12,command=audiop)
b4.grid(row=5,column=3)

def speak():
     capture=root.Recognizer()
     with root.Microphone() as source:
      #print("say")
      text.insert(tk.INSERT,'Speak\n')
      audio=capture.listen(source)
      text.insert(tk.INSERT,'Done\n')
      #print("done")
      speak1=capture.recognize_google(audio)
      speak2=capture.recognize_google(audio,language='hi-IN')
      try:
          text.insert(tk.INSERT,speak1)
          text.insert(tk.INSERT,speak2)
        #print(capture.recognize_google(audio))
        #print(capture.recognize_google(audio,language='hi-IN'))
      except:
        #print("sorry")
        text.insert(tk.INSERT,'Somethink wrong')

b1 = Button(window, text="Speak", width=12, command=speak)
b1.grid(row=5, column=1)

window.mainloop()
