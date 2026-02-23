import sys
import pyttsx3
import speech_recognition as sr
import pyautogui
import time
import os
import pygetwindow as gw

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.dynamic_energy_threshold = True
    with sr.Microphone() as source:
        print("Calibrating mircrophone...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = r.listen(source)

    try: 
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower() 
    except sr.UnknownValueError:
        print("sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry Calero, Network di disturb bad")
        return ""
   
while True:
    command = listen()
    if command:
        if __name__ == "__main__":
            print(sys.executable)
            speak("Hello Calero, how can I assist you today?")
        running = route_command(command)
        if not running:
            break

    def open_app(app_name):
        speak(f"Opening {app_name}...")
        os.system("start " + app_name)

    def type_text(text):
        time.sleep(1)
        pyautogui.write(text, interval=0.05)

    def close_window():
        speak("closing current window")
        pyautogui.hotkey("alt", "f4")

    def minimize_window():
        speak("minimizing current window")
        pyautogui.hotkey("win", "down") 

    def spotify_control(command):
        try:
            window = gw.getWindowsWithTitle("Spotify")
            if window:
                win = window[0]
                win.activate()
                time.sleep(0.5)

        except:
            speak("Could not control Spotify.")
        
        speak(f"Controlling spotify with command: {command}")
        if command == "play":
            pyautogui.press("space")
        elif command == "pause":
            pyautogui.press("space")
        elif command == "next":
            pyautogui.hotkey("ctrl","right")
        elif command == "previous":
            pyautogui.hotkey("ctrl","left")

    def route_command(command):
        if "open chrome" in command:
            open_app("chrome")

        elif "open notepad" in command:
            open_app("notepad")

        elif "type" in command:
            text = command.replace("type", "").strip()
            type_text(text)
            speak("done typing")

        elif "spotify" in command:
            open_app("spotify")
            time.sleep(2)
            spotify_control("play")

        elif "pause spotify" in command:
            spotify_control("pause")

        elif "next song" in command or "next track" in command:
            spotify_control("next")

        elif "previous song" in command or "previous track" in command:
            spotify_control("previous")

        elif "time" in command:
            now = time.strftime("%H:%M:%S")
            speak(f"The time is {now}")

        elif "close window" in command:
            close_window()

        elif "minimize window" in command:
            minimize_window()

        elif "stop" in command:
            speak("goodbye")
            return False
        else:
            speak("I did not understand that Calero.")

        return True