import speech_recognition as sr
import pyttsx3
import webbrowser
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi="ac70e104d17d44b599dee607f9ca6fa6"

def get_news():
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
        response = requests.get(url)
        news_data = response.json()
        
        if news_data.get("status") == "ok":
            articles = news_data.get("articles", [])
            headlines = [article["title"] for article in articles[:5]]  # Get top 5 headlines
            
            if headlines:
                speak("Here are the latest news headlines.")
                for idx, headline in enumerate(headlines, 1):
                    speak(f"News {idx}: {headline}")
            else:
                speak("No news found at the moment.")
        else:
            speak("Sorry, I couldn't fetch the news.")
    
    except Exception as e:
        speak("There was an error fetching the news.")
        print(f"Error: {e}")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    if "open google" in command.lower():
        speak("opening google")
        webbrowser.open("https://google.com")
    elif "open facebook" in command.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command.lower():
        speak("opening youtube")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://linkedin.com")
    elif command.startswith("play"):
        speak("playing")
        webbrowser.open("https://www.youtube.com/watch?v=cNGjD0VG4R8")

    elif "open news" in command.lower():
        get_news()
    elif "kritarth" in command.lower():
        speak("KRITARTH IS THE ONE WHO DEVELOPED ME . AND HE IS A BCA STUDENT WHO IS SPECIALIZED IN THE FIELD OF TECHNOLOGY AND ARTIFICIAL INTELLIGENCE.   HE WAS BORN IN A SMALL TOWN OF UTTARAKHAND CALLED GADORA.  AND HE IS VERY DEDICATED AND PASSIONAITE TOWARDS HIS WORK, OTHER THAN THAT HE IS A PROFESSIONAL BADMINTON PLAYER. ")
    elif "rest" in command.lower():
        speak("THANK YOU ")
    elif "tell me " in command.lower():
        speak("HY I AM ROMEO , A VIRTUAL ASSISTANT DESIGNED AND DEVELOPED BY KRITARTH. I CAN HELP YOU IN FINDING THE SOLUTION FOR EVERYTHING. IF YOU HAVE ANY DOUBT PLEASE BE FREE TO ASK ME. ")

if __name__ == "__main__":
    speak("Initializing romeo...")

    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                word = recognizer.recognize_google(audio)

                if word.lower() == "romeo":
                    speak("Yes kritarth")
                    
                    with sr.Microphone() as source:
                        print("Romeo Active...")
                        recognizer.adjust_for_ambient_noise(source)
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        processCommand(command)
                       

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
        except sr.RequestError:
            print("Speech Recognition service is unavailable.")
        except Exception as e:
            print(f"Error: {e}")

