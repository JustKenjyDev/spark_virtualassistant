import os
import sys

def tts(message):
    if sys.platform == 'darwin':
        tts_engine = 'say'
        return os.system(tts_engine + ' ' + message)
    elif sys.platform == 'linux2' or sys.platform == 'linux':
        tts_engine = 'espeak -vnl'
        return os.system(tts_engine + ' ' + message)


tts('de_appel_valt_niet_ver_van_de_boom')
