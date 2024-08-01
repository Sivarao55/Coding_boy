import speech_recognition as sa
import pyttsx3
import pywhatkit
import wikipedia
from datetime import datetime
from datetime import date
import webbrowser

def process(question):
    if 'what are you' in question:
        print("I am waiting for your question")
        talk("I am waiting for your question")
        return True
    elif 'hi' in question:
        print("hi sai my name is also saranya")
        talk("hi sai my name is also saranya")
        return True
    elif 'how are you' in question:
         print("I am good,thank you.How can I help you")
         talk("I am good,thank you.How can I help you")
         return True
    elif 'play' in question:
        question = question.replace('play','playing')
        print(question)
        pywhatkit.playonyt(question)
        return True
    elif 'who is' in question:
        question = question.replace('who is','')
        print(wikipedia.summary(question,1))
        talk(wikipedia.summary(question,1))
        return True
    elif 'time' in question:
        time = datetime.today().time().strftime("%I:%M:%p")
        print(time)
        talk(time)
        return True
    elif 'time' in question:
        time = datetime.today().time().strftime("%I:%M:%p")
        print(time)
        talk(time)
        return True
    elif 'Google' in question:
        print("browser is opening.....")
        url='https://google.com'
        webbrowser. get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'). open(url)
        
    elif 'YouTube' in question:
        print("youtube is opening.....")
        url='https://youtube.com'
        webbrowser. get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'). open(url)
        return True
    elif 'hotstar' in question:
        print("opening Hotstar.....")
        url="https://www.hotstar.com/in"
        webbrowser. get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'). open(url)
        return True
    elif 'Amazon' in question:
        print("opening amazon'......")
        url='https://www.amazon.in'
        webbrowser. get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'). open(url)
        return True
    elif 'Flipkart' in question:
        print("opening flipkart'......")
        url='https://www.flipkart.com'
        webbrowser. get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'). open(url)
        return True
    elif 'Prime video' in question:
        print("prime video is opening.....")
        url='https://www.primevideo.com/?ref_=dvm_pds_amz_in_as_s_g_72_mkw_sfQQR2NKb-dc&mrntrk=pcrid_386629063601_slid__pgrid_82649959567_pgeo_1007740_x__ptid_kwd-308511887188'
        webbrowser. get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'). open(url)
        return True    
    elif 'bai' in question:
        print(" my explantion is over so bye ")
        talk("my explantion is over so bye ")
        return False
    else:
        print("I don't know your question")
        talk("I don't know your question")
        return True
def talk(answer):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(answer)
    engine.runAndWait()
def getQuestion():       
    r = sa.Recognizer()

    with sa.Microphone() as source:
        print("Sivarao say something")
        talk("Sivarao say something")

        audio = r.listen(source)
        try:
            print(r.recognize_google(audio))
            question = r.recognize_google(audio)
            if 'Sai' in question:
                question = question.replace('Sai','')
                print(question)
                return question
           
            else:
                print("call me sai ")
                talk("call me sai ")
                return "notwithme"
        except sa.UnknownValueError:
            print("please tell me again")
            talk("please tell me again")
            return True

canAskQuestion = True
while canAskQuestion:
    question = getQuestion()
    if(question=="notwithme"):
        print("okay carry on with your friends,bye!")
        talk("okay carry on with your friends,bye!")
        canAskQuestion = True
    else:
        CanAskQuestion = process(question)
