import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import sys

# ─── JARVIS INIT ───────────────────────────────────────────────
engine = pyttsx3.init()
engine.setProperty('rate', 175)       # speaking speed
engine.setProperty('volume', 1.0)     # max volume

# Try to set a deeper voice (more Jarvis-like)
voices = engine.getProperty('voices')
for voice in voices:
    if 'male' in voice.name.lower() or 'david' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.8     # how long silence = end of sentence


def speak(text):
    """Jarvis speaks."""
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen for a voice command. Returns lowercase string or None."""
    with sr.Microphone() as source:
        print("\n[Listening...]")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            command = recognizer.recognize_google(audio).lower()
            print(f"YOU: {command}")
            return command
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            speak("Didn't catch that. Say it again.")
            return None
        except sr.RequestError:
            speak("Speech service is down. Check your internet.")
            return None


def handle_command(command):
    """Process the command and respond."""

    # ── wake/personality ──
    if "oil up" in command:
        speak("Oiling up. Ready to dominate.")

    elif "who are you" in command or "introduce yourself" in command:
        speak("I am Jarvis. Your personal AI assistant. Built by Hamza.")

    elif "hello" in command or "hey jarvis" in command or "hi" in command:
        speak("Online. What do you need?")

    # ── time & date ──
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"It is {now}.")

    elif "date" in command:
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {today}.")

    # ── browser & search ──
    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://youtube.com")

    elif "open github" in command:
        speak("Opening GitHub.")
        webbrowser.open("https://github.com")

    elif "open fiverr" in command:
        speak("Opening Fiverr. Time to get clients.")
        webbrowser.open("https://fiverr.com")


    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            speak(f"Searching for {query}.")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            speak("What should I search for?")

    # ── system ──
    elif "open vs code" in command or "open vscode" in command:
        speak("Launching VS Code.")
        os.system("code")

    elif "open notepad" in command:
        speak("Opening Notepad.")
        os.system("notepad")

    elif "screenshot" in command:
        speak("Taking screenshot.")
        os.system("snippingtool")

    # ── motivation (Hamza mode) ──
    elif "motivate me" in command or "motivation" in command:
        speak("You started with nothing. You built me in one night. No plan B. Keep going.")

    elif "solo leveling" in command:
        speak("Arise. You are the shadow monarch. Now get back to work.")

    elif "goggins" in command:
        speak("Stay hard. Who's gonna carry the boats?")

    # ── shutdown ──
    elif "shutdown" in command or "goodbye" in command or "bye jarvis" in command:
        speak("Shutting down. Stay hard.")
        sys.exit(0)

    else:
        speak(f"Command not recognized: {command}. Add it to my brain.")


# ─── MAIN LOOP ─────────────────────────────────────────────────
def main():
    speak("Jarvis online. ready for domination. whats in your mind?.or you hit your ai usage limit. will u switch to a diffrent ai for now?? Awaiting commands.")

    while True:
        command = listen()
        if command:
            handle_command(command)


if __name__ == "__main__":
    main()
