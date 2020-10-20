from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyttsx3
import speech_recognition as sr
import datetime
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id) you can also use Female version
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-pk')
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'jarvis' in query:
            speak("Yes please! KAMI-360")


        if 'send message on whatsapp' in query:
            speak("Sir,whome u want to send message")
            time.sleep(5)
            name=takeCommand().lower()
            #slicing it
            sliced_name=""
            for i in name.split(" "):
                i = i.capitalize()
                sliced_name+=i + " "
            print(sliced_name)

            driver = webdriver.Chrome()
            driver.get("https://web.whatsapp.com/")
            speak("Please scan the QR code for whatsapp web")
            time.sleep(15)
            p=driver.find_element_by_css_selector(f"span[title={sliced_name}]")
            p.click()
            speak("what should i say")
            time.sleep(5)
            text=takeCommand().lower()
            put = driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
            put.send_keys(text)
            put.send_keys(Keys.RETURN)
            speak("Successfully sent")

