#https://www.facebook.com/roshan.philipines/posts/2767126086910368
# Subscribed by Roshaen Kumar
import pyautogui as pg
from time import sleep
import sys
sleep(3)

class Spam:
    def __init__(self, word, n):
        self.word = word
        self.n = n
    def spamer(self, word, n):
        i=0
        for i in range(self.n):
            sleep(1)
            pg.typewrite(self.word)
            pg.press("enter")


ls = sys.argv[1:]
print(ls)
word = ls[0]
n = ls[1]
        
spam1 = Spam("Hello",25)
spam1.spamer(word, n)
