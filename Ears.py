import speech_recognition as sr
import pyaudio as pa

class Ears():
    recognizer = sr.Recognizer()

    def capture_voice_input(self):
        with sr.Microphone() as source:
            print("Listening...")
            # Need a limit on how long it listen for, Else it will keep listening until it finishes.
            audio = self.recognizer.listen(source)
        return audio

    def convert_voice_to_text(self, audio):
        try:
            text = self.recognizer.recognize_google(audio)
            print("You said: " + text)
        except sr.UnknownValueError:
            text = ""
            print("Sorry, I didn't understand that.")
        except sr.RequestError as e:
            text = ""
            print("Error; {0}".format(e))
        return text

    def get_words(self):
        return self.convert_voice_to_text(self.capture_voice_input())

