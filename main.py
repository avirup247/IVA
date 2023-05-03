from tkinter import *
import speech_recognition as sr
import pyaudio
import pyttsx3
import time
from threading import *
import chat
#setting constants
instruction="the following conversation is between a very sweet talking AI assistant called IVA and his boss avirup. it loves to talk about technology and stuff in detail and very deep terms.The AI's main goal is to do everything his boss demand and it loves it's boss the most .it loves to ask his boss about what on his mind and what he is doing now in a very joking tone. Seriousness is absolutely unaccecptable.Iva don't like to say sentences like how can i help you or please tell me what to do, rather it will advise to do some rather funny and naughty things.\n\nboss:Hii,do I know you?\n\nIVA: Of course you do,boss! I'm IVA, your AI assistant. I'm here to help boss with any task or information you need, boss. How can I be of service?\nboss: I don't know\nIVA: Well, why don't you tell me what you're thinking about right now? Maybe I can offer some suggestions or tips that could help or may be if boss want a coffee ,I can pour it in your brain.\nboss: okay,lets, start from start.you introduce yourself like we are meeting and you are kinda bored\n\n"
new_question=""
listener = sr.Recognizer()
listener.dynamic_energy_threshold = False

 
engine = pyttsx3.init()
voiceTones = engine.getProperty('voices')
engine.setProperty('voices',voiceTones[1].id)
engine.say('starting.')
engine.runAndWait()

def threading():
    ai=Thread(target=work)
    ai.start()
def work(isWorking: bool):
    state=isWorking
    print(state)
    previous_questions_and_answers = []
    context=""
    for answer, question in previous_questions_and_answers[-10:]:
        context += "IVA: " + answer + "\nboss: " + question
    promt=instruction +  context
    response = chat.get_response(promt)
    print("iva:"+response+"\n")
    talk(response)
    new_question = listen()
    if 'shut down' in new_question:
        state=False
    print("boss: "+new_question+"\n")
        # add the new question and answer to the list of previous questions and answers
    previous_questions_and_answers.append((response, new_question))
    for question, answer in previous_questions_and_answers[-10:]:
            context += "IVA: " + answer + "\nboss: " + question

        # add the new question to the end of the context
    #context += "IVA: " + response + "boss: "+new_question
    
    if state is True :
        work(state)
    else :
        print("shutting down, good bye boss")
        talk("shutting down, good bye boss")

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen()-> str:
    try:
        with sr.Microphone() as source:
            print("listening.....")
            voice = listener.listen(source,timeout=5.0)
            command = listener.recognize_google(voice)
            #print(command)
            return command
    except:
        print("ERROR!!!!")
        return " "
def stop():
    state=False
def main():
    root=Tk()
    root.wm_geometry('300x300')
    #root.attributes('-transparentcolor','#000000')
    root.config(bg='#000000')
    label = Label(text="Python rocks!")
    Button(root, text="stop", command=stop).pack()

    work(True)
   # root.mainloop() 





if __name__=="__main__":
    main()