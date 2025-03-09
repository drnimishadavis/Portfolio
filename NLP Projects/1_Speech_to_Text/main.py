import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

recognizer=sr.Recognizer()
translator=Translator()

def recognize_speech():
    with sr.Microphone() as source:
        print("Listening.......!!")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)

    try:
        print("Reconginizing speech...")
        text=recognizer.recognize_google(audio)
        print(f"sppech recognized : {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio..")
    except st.RequestError:
        print("Error with the request;please check your internet connection")
        return None

def translate_text(text,target_language):
    translated=translator.translate(text,dest=target_language)
    print(f"translated text: {translated.text}")
    return translated.text

def text_to_speech(text,language):
    tts=gTTS(text=text,lang=language,slow=False)
    tts.save("trans_audio.mp3")
    os.system("start trans_audio.mp3")



if __name__ == "__main__":
    target_language="de"
    print("speak in your native language...")
    speech_text=recognize_speech()
    if speech_text:
        translated_text=translate_text(speech_text,target_language)
        text_to_speech(translated_text,target_language)


# developed by Nimisha Davis
# https://linktr.ee/drnimishadavis











    