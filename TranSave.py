from googletrans import Translator
from playsound import playsound
from gtts import gTTS
import re
import os
import time

translator = Translator()
dest = input("Enter dest: ")
try:
    while True:
        f = open("‪Vocabulary.txt","r+",encoding='utf-8')
        t = translator.translate(input("Enter Text: "), dest)
        print('\n' + t.text + '\n' )
        sound = gTTS(t.origin)
        sound.save('sound\\' + t.origin + '.mp3')
        playsound('sound\\' + t.origin + '.mp3')
        repeated = re.findall(t.origin, str(f.read()))
        
        if (t.text != "") and (t.text != t.origin) and (len(repeated) == 0):
            f.write(str('\n' + t.origin + '\t' + t.text + '\n'))
        f.close()
except:
    print("Thanks for using, all your translations has been saved.")
