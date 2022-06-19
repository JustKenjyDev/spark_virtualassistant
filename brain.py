import speech_recognition as sr
import os
import sys
from gtts import gTTS
from playsound import playsound
import python_weather
import pyjokes
from deep_translator import GoogleTranslator
import weatherstatus as getweather
from datetime import datetime
import yaml
import wikipedia as wiki
import joke as getJoke

#WAKE WORD EERST!

while True:
 WAKE = "hey spark"
 end = None

 message = ''
 r = sr.Recognizer()

 while True:
  try:

     with sr.Microphone() as source:
             print('Geef bericht:')
             audio = r.listen(source)
             message = r.recognize_google(audio, None, 'en_EN')

     if message.count(WAKE) > 0:    
             break
     else:
             console.log('Didnt understand')
  except:
             pass
            
            
 try:
   tts = gTTS('Ik luister.', lang="nl")
   tts.save("listening.mp3")
   playsound("listening.mp3")
   
   with sr.Microphone() as source:
         audio = r.listen(source)
         message = r.recognize_google(audio, None, 'nl_BE')

         if 'Wat is jouw naam' in message:
             tts = gTTS(
                    'Hallo mijn naam is spark, jouw virtuele assistent.', lang="nl")
             tts.save("naam.mp3")
             playsound("naam.mp3")
         elif 'Hoe is het weer' in message:
             tts = gTTS(getweather.weatherstatus("Lokeren"), lang = "nl")
             tts.save("weather.mp3")
             playsound("weather.mp3")
             os.remove("weather.mp3")
         elif 'Zeg een mop' in message:
             joke = pyjokes.get_joke(language="en", category="all")
             print(joke)
             translated = GoogleTranslator(
                     source='auto', target='nl').translate(joke)
             print(translated)
             tts = gTTS(translated, lang="nl")
             tts.save("joke.mp3")
             playsound("joke.mp3")
             os.remove("joke.mp3")
         elif 'Hoe laat is het' in message:
             now = datetime.now()
             currentTime = now.strftime("%H:%M")
             tts = gTTS(currentTime, lang = "nl")
             tts.save("currenttime.mp3")
             playsound("currenttime.mp3")
             os.remove("currenttime.mp3")
         elif 'Wie is jouw maker' in message:
             tts = gTTS(
                     'Ik ben ontworpen door Van Reeth Kenjy.', lang="nl")
             tts.save("creator.mp3")
             playsound("creator.mp3")
             
         elif 'zoek naar' in message:
             try:
              search = message[9:end]
              wiki.set_lang("nl")
              tts = gTTS(wiki.summary(search, sentences = 2), lang = "nl")
              tts.save("wiki.mp3")
              playsound("wiki.mp3")
              os.remove("wiki.mp3")
             except:
              tts = gTTS("Sorry, Ik heb niks gevonden.", lang = "nl")
              tts.save("nonefound.mp3")
              playsound("nonefound.mp3")
              os.remove("nonefound.mp3")
       
         elif 'Ik verveel me' in message:
             tts = gTTS('Ik kan daar wel bij helpen. Wilt u een mop horen?')
             tts.save("verveelmij.mp3")
             playsound("verveelmij.mp3")
             os.remove("verveelmij.mp3")
             audio = r.listen(source)
             answer = r.recognize_google(audio, None, 'nl_BE')
             if 'ja' in answer:
                 tts = gTTS(getJoke(), lang = "nl")
                 tts.save("joke.mp3")
                 playsound("joke.mp3")
                 os.remove("joke.mp3")
             else:
                 pass
         elif 'Waar ben je voor gemaakt' in message:
             tts = gTTS(
                     'Ik ben ontworpen als een eindproject. Mijn functie is voor het leven van u gemakkelijker te maken en uw te assisteren met uw vragen en andere functies.', lang="nl")
             tts.save("function.mp3")
             playsound("function.mp3")
         
            

   #Google Search
   #'Ik verveel me' -> Suggestie grap of feitje -> Needs testing 
   #EXTRA: Youtube/Spotify player


         else:
            tts = gTTS("Zei je dit?:" + message, lang = "nl")
            tts.save("herhaling.mp3")
            playsound("herhaling.mp3")

 except sr.UnknownValueError:
           print('Sorry, ik kon je niet verstaan')
           tts = gTTS('Sorry, ik kon je niet verstaan', lang="nl")
           tts.save("ValueError.mp3")
           playsound("ValueError.mp3")
           os.remove("ValueError.mp3")

         
