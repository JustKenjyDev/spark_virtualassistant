import pyjokes
from deep_translator import GoogleTranslator

def getJoke():

      joke = pyjokes.get_joke(language="en", category="all")
      return GoogleTranslator(source='auto', target='nl').translate(joke)
      
print(getJoke())
