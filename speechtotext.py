import asyncio
import speech_recognition as sr
import requests

recognizer = sr.Recognizer()
mic = sr.Microphone()

def send_message_to_rasa(text):
    url = 'http://localhost:5005/webhooks/rest/webhook'  # Default Rasa REST endpoint
    payload = {
        "sender": "user",
        "message": text
    }
    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to send message to Rasa bot.")
        return None



async def recognize_speech():
    with mic as source:
        print("Listening... Say 'I'm done' to stop.")

        while True:
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")
                
                #speech ----> Rasa
                bot_response = send_message_to_rasa(text)
                
                
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
