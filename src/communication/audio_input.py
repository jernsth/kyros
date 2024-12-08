import pyaudio
import speech_recognition as sr


def recognize_speech_from_mic():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Listening...")

        try:
            # Capture audio
            audio = recognizer.listen(source, timeout=10)  # 10 seconds timeout
            print("Processing...")

            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google_cloud(audio, language="en_US")
            print(f"Recognized Text: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Error with the recognition service: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


recognize_speech_from_mic()