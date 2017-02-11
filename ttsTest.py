import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1

text_to_speech = TextToSpeechV1(
    username='573eea08-b036-476e-8701-ba6afe44e12a',
    password='5qir686Ar1sz',
    x_watson_learning_opt_out=True)  # Optional flag

print(json.dumps(text_to_speech.voices(), indent=2))

with open(join(dirname(__file__), '../output.wav'),
          'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize('Hello See Em You!', accept='audio/wav',
                                  voice="en-US_AllisonVoice"))

print(
    json.dumps(text_to_speech.pronunciation(
        'Watson', pronunciation_format='spr'), indent=2))

print(json.dumps(text_to_speech.customizations(), indent=2))