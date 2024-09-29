import speech_recognition
from RealtimeSTT import AudioToTextRecorder
import pyttsx3
import threading
import datatransfare
import pygame
import utilitys

#Task Queue
Make_Record = False

tts = pyttsx3.init()
tts_lock = threading.Lock()

Audio = None

font = None

animated_text = utilitys.AnimatedText("", font, (255, 255, 255), (960, 540), speed=2)

def record():
    global recognizer
    try:
        with speech_recognition.Microphone() as mic:
            animated_text.reset("Recording...")
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio_data=audio, language="de_DE")
            text.lower()
            print(text)
            animated_text.reset("Loading...")
    except speech_recognition.UnknownValueError:
        animated_text.reset("Something went wrong. Please try it again")

        recognizer = speech_recognition.Recognizer()





    return text

def say(text):
    # Say the antwort
    tts.say(text)
    tts.runAndWait()
    print("Played Audio")

def main():
    global animated_text  # Zugriff auf die animierte Textinstanz
    text = record()
    print(text)
    datatransfare.send_string(text, '127.0.0.1', 55555)
    antwort = datatransfare.receive_string(55554)

    print(antwort)
    # Text an die animierte Textklasse übergeben und animieren
    animated_text.reset(antwort)

    say(antwort)


frames = [pygame.image.load("assets/orb/frame_1.png"),
          pygame.image.load("assets/orb/frame_1.png"),
          pygame.image.load("assets/orb/frame_1.png"),
          pygame.image.load("assets/orb/frame_1.png"),
          pygame.image.load("assets/orb/frame_2.png"),
          pygame.image.load("assets/orb/frame_2.png"),
          pygame.image.load("assets/orb/frame_2.png"),
          pygame.image.load("assets/orb/frame_2.png"),
          pygame.image.load("assets/orb/frame_3.png"),
          pygame.image.load("assets/orb/frame_3.png"),
          pygame.image.load("assets/orb/frame_3.png"),
          pygame.image.load("assets/orb/frame_3.png"),
          pygame.image.load("assets/orb/frame_4.png"),
          pygame.image.load("assets/orb/frame_4.png"),
          pygame.image.load("assets/orb/frame_4.png"),
          pygame.image.load("assets/orb/frame_4.png"),
          pygame.image.load("assets/orb/frame_5.png"),
          pygame.image.load("assets/orb/frame_5.png"),
          pygame.image.load("assets/orb/frame_5.png"),
          pygame.image.load("assets/orb/frame_5.png"),
          pygame.image.load("assets/orb/frame_6.png"),
          pygame.image.load("assets/orb/frame_6.png"),
          pygame.image.load("assets/orb/frame_6.png"),
          pygame.image.load("assets/orb/frame_6.png"),
          pygame.image.load("assets/orb/frame_7.png"),
          pygame.image.load("assets/orb/frame_7.png"),
          pygame.image.load("assets/orb/frame_7.png"),
          pygame.image.load("assets/orb/frame_7.png")
          ]

recordbutton = utilitys.AnimatedButton(20, 20, frames, scale=1)

def GameLoop(clock, screen):
    global Make_Record
    global Audio
    run = True
    while run:
        # Quit pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False



        screen.fill((0, 0, 0))  # Bildschirm leeren
        # Aktualisiere den animierten Text
        animated_text.update()
        animated_text.draw(screen)

        if recordbutton.draw(screen):
            print("Run main")
            Make_Record = True


        pygame.display.update()
        clock.tick(60)

def config_pygame():
    global font
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Holowmat")
    clock = pygame.time.Clock()
    GameLoop(clock=clock, screen=screen)


if __name__ == '__main__':
    recognizer = speech_recognition.Recognizer()
    pygame_thead = threading.Thread(target=config_pygame)
    pygame_thead.start()
    while True:
        if Make_Record == True:
            print("Run in Main Thread")
            Make_Record = False
            main()
