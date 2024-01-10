import asyncio
import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()

async def recognize_speech():
    with mic as source:
        print("Listening... Say 'I'm done' to stop.")

        while True:
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")

                if "i'm done" in text.lower():
                    print("Recognition stopped.")
                    break  # Exit the loop when 'I'm done' is detected

            except sr.UnknownValueError:
                print("Sorry, could not understand the audio.")
            except sr.RequestError:
                print("Sorry, could not request results; check your internet connection.")

async def main():
    await recognize_speech()

if __name__ == "__main__":
    asyncio.run(main())
