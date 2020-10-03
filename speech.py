# https://m.facebook.com/story.php?story_fbid=101362998411817&id=100056143503621
# sir I made my Id on Fb after watching your video , but it will remain as it is.
# subscribed by code house


import io
import pygame
from gtts import gTTs

def speak(text):
    with io.BytesIO() as file:
        gTTs(text=text, lang="en").write_to_fp(file)
        file.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue


if __name__ == '__main__':
    text = input("what should i say? >")
    speak(text)
