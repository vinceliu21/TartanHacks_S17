
'''
This script will manage the budgement management aspect of 
our IBM Watson TartanHacks Project. It keeps running until the
user signifies that he is done maintaining control of his budget.
At that point, control will then be returned to the Polling phase
of the system.

Input: There is no input as this script will be called 
when the previous component of the system recognizes the phrase
"Budget"

Output: Complete of all budget management tanks

'''

import json

from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud import TextToSpeechV1

import simpleaudio as sa
import wave, struct, math

from SaveAudio import save_audio
from recorder import Recorder

import pandas as pd


def play_audio(text):
    text_to_speech = TextToSpeechV1(
        username='573eea08-b036-476e-8701-ba6afe44e12a',
        password='5qir686Ar1sz',
        x_watson_learning_opt_out=True)


    with open(join(dirname(__file__), 'resources/audio.wav'), 'wb') as audio_file:
        audio_file.write(text_to_speech.synthesize(text, 
            accept='audio/wav', voice="en-US_AllisonVoice"))

    
    wave_obj = sa.WaveObject.from_wave_file("resources/audio.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
    


def receive_audio(speech_file):
    speech_to_text = SpeechToTextV1(username='799f8c1d-67cf-4c0e-b833-76eeab3a90a9', password='H3UE0oRRdNdx', x_watson_learning_opt_out=False)

    with open(join(dirname(__file__), speech_file), 'rb') as audio_file:
        text = json.dumps(speech_to_text.recognize(audio_file, content_type='audio/wav', timestamps=True, word_confidence=True), indent=2)

    return text



def watson_budget(name, day):

    running = True
   
    df = pd.read_csv('resources/budget.csv')
    df1 = df.set_index("Name")
    play_audio("What would you like to do with your budget today?")

    
    while running:
        #save_audio() 
        recorder = Recorder('resources/1.wav')
        recorder.record_to_file()
        text = receive_audio('resources/1.wav')
        print(text)
        print(type(text)) 
        if "close" in text:
            play_audio("Alright then goodbye!")
            running = False
        elif "spend" in text:
            play_audio("Here is your daily summary!")
            amount = df1.loc[name, day]
            play_audio('Okay, ' + name + ' You spent ' + str(amount) + ' dollars today.') 
            play_audio("What else would you like to know?")
        elif "register" in text:
            play_audio("Sure thing, how much money did you spend today?")
            #save_audio()
            #recorder = Recorder('resources/1.wav')
            recorder.record_to_file()
            text = receive_audio('resources/1.wav')
            print(text)
            df1.loc[name,day] += 5
            df1.to_csv('resources/budget.csv')
            play_audio("Okay saved it, what else would you like to know.")
            
        else:
            play_audio("Sorry I did not get that, please repeat your request!")



    return
        
        
    
        

#watson_budget("Edward", "Friday")








            
