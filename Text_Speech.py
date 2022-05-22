# -*- coding: utf-8 -*-
"""
Created on Wed May 11 17:32:15 2022

@author: hp
"""

# Text to Speech Conversion

import pyttsx3
text_speech = pyttsx3.init()
answer = input("What do I speak? ")
voices = text_speech.getProperty('voices')
#print(voices)
text_speech.setProperty('voice', voices[1].id)
text_speech.say(answer)
text_speech.runAndWait()



