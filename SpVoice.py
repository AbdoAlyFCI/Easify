#required library for speech recognition
import speech_recognition as sr


#Step 2 get result from Google voice recognition API
# obtain audio from the microphone
def check_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)


    # recognize speech using Google Speech Recognition
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return "no any rec"
    except sr.RequestError as e:
        return "no any rec"



