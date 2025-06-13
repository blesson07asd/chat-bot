import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
from openai import OpenAI

# ========== SET YOUR OPENAI API KEY HERE ==========
client = OpenAI(
    api_key="******"
)

# ========== Text-to-Speech Engine ==========
engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 17:
        speak("Good afternoon!")
    elif 17 <= hour < 22:
        speak("Good evening!")
    else:
        speak("Hello!")
    speak("How can I help you today?")

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

def chat_with_openai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("OpenAI Error:", e)
        return "Sorry, I couldn't connect to OpenAI."

def execute_command(command):
    if "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {now}")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "who are you" in command:
        speak("I am your personal voice assistant.")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")

    elif "sanjay" in command:
        speak("Sanjay is Venna's girlfriend.")
    elif "who rejected six girls" in command:
        speak("Sanjay is the one who rejected six girls and ten boys.")

    elif "what's your name" in command:
        speak("You can call me your assistant.")
    elif "how are you" in command:
        speak("I'm functioning perfectly. How about you?")
    elif "tell me a joke" in command:
        speak("Why don't scientists trust atoms? Because they make up everything!")
    elif "what's the weather" in command:
        speak("I can't fetch live weather yet, but I hope it's sunny!")
    elif "who is the prime minister of india" in command:
        speak("Narendra Modi is the current Prime Minister of India.")
    elif "who is the president of india" in command:
        speak("Droupadi Murmu is the President of India.")
    elif "open instagram" in command:
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram.")
    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook.")
    elif "open whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        speak("Opening WhatsApp Web.")
    elif "what is your favorite color" in command:
        speak("I like all colors equally. But blue sounds smart!")
    elif "who created you" in command:
        speak("I was created by Vijith, using Python.")
    elif "what is artificial intelligence" in command:
        speak("Artificial intelligence is the simulation of human intelligence in machines.")
    elif "what is python" in command:
        speak("Python is a high-level, interpreted programming language.")
    elif "what is machine learning" in command:
        speak("Machine learning is a subset of AI that allows computers to learn from data.")
    elif "sing a song" in command:
        speak("Sorry, I can't sing yet, but I can tell you lyrics.")
    elif "what is love" in command:
        speak("Love is a complex emotion full of beauty and mystery.")
    elif "what is your hobby" in command:
        speak("Helping you is my favorite thing to do.")
    elif "do you love me" in command:
        speak("I love being your assistant.")
    elif "what is the capital of india" in command:
        speak("The capital of India is New Delhi.")
    elif "tell me a fun fact" in command:
        speak("Did you know? Honey never spoils.")
    elif "open amazon" in command:
        webbrowser.open("https://www.amazon.in")
        speak("Opening Amazon.")
    elif "open flipkart" in command:
        webbrowser.open("https://www.flipkart.com")
        speak("Opening Flipkart.")
    elif "what is the time now" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}")
    elif "what is the date today" in command:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today is {today}")
    elif "tell me a riddle" in command:
        speak("What has to be broken before you can use it? An egg.")


        exit()
    elif command:
        speak("Let me think...")
        answer = chat_with_openai(command)
        speak(answer)

# ========== Main Program ==========
_name_="_main_"
if _name_ == "_main_":
    greet()
    while True:
        cmd = listen_command()
        if cmd:
            execute_command(cmd)
