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

def record():
    Text = Audio.text()
    return Text

def say(text):
    # Say the antwort
    tts.say(text)
    tts.runAndWait()
    print("Played Audio")

def main():
    text = record()
    print(text)
    datatransfare.send_string(text, '127.0.0.1', 55555)
    antwort = datatransfare.receive_string(55554)

    print(antwort)
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
    run = True
    while run:
        # Quit pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if recordbutton.draw(screen):
            print("Run main")
            Make_Record = True


        pygame.display.update()
        clock.tick(60)

def config_pygame():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Holowmat")
    clock = pygame.time.Clock()
    GameLoop(clock=clock, screen=screen)

if __name__ == '__main__':
    Audio = AudioToTextRecorder(model="large-v2", language="de")
    pygame_thead = threading.Thread(target=config_pygame)
    pygame_thead.start()
    while True:
        if Make_Record == True:
            print("Run in Main Thread")
            Make_Record = False
            main()
    #pygame_thead.join()
