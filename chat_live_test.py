import speech_recognition as sr
import openai
import pyttsx3

def listen_for_activation():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for activation...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        
        #once the mic is activated, it will listen for your activation code like Siri or OK google.
        if "hey northstar" in text.lower(): 
            print("Activation code received.")
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id) # female voice
            
            #once it's activited, you will hear the audio below.
            engine.say("How can I help you?")
            engine.runAndWait()
            return listen_for_question()
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return listen_for_question()

def listen_for_question():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for question...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        if "new question" in text.lower():
            print("New question detected.")
            return listen_for_activation()
        else:
            print("Question received:", text)
            return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")

def speak_answer(answer):
    engine = pyttsx3.init()
    engine.say(answer)
    engine.runAndWait()

openai.api_key = "" #enter your API key here

question = listen_for_activation()
if question:
    while True:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=question,
            max_tokens=3000,
            n=1,
            stop=None,
            temperature=0.5,
        )
        answer = response.choices[0].text
        print("Answer:", answer)
        speak_answer(answer)
        question = listen_for_question()
