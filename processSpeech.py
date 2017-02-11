from AudioFile import AudioFile
from recorder import Recorder
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
from watson_developer_cloud import SpeechToTextV1


def tts(text):
    text_to_speech = TextToSpeechV1(
        username='573eea08-b036-476e-8701-ba6afe44e12a',
        password='5qir686Ar1sz',
        x_watson_learning_opt_out=True)

    #  Initial greeting
    with open(join(dirname(__file__), 'resources/greeting.wav'),
              'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize(text,
                                      accept='audio/wav',
                                      voice='en-US_AllisonVoice'))


def stt(filename):
    speech_to_text = SpeechToTextV1(
        username='799f8c1d-67cf-4c0e-b833-76eeab3a90a9',
        password='H3UE0oRRdNdx',
        x_watson_learning_opt_out=False
    )

    with open(join(dirname(__file__), filename), 'rb') as audio_file:
        result = (speech_to_text.recognize(
            audio_file, content_type='audio/wav', timestamps=False,
            word_confidence=False))
    return result


def processSpeech(name):
    '''
    Asks name what they want to do and processes
    the speech into text.

    @param name  string of name from face recognition
    @return      extracted keyword from speech
    '''
    #  Initial greeting
    tts('Hello ' + name + '. \
        What can I do for you today?')
    audio = AudioFile('resources/greeting.wav')
    audio.play()
    audio.close()

    #  Wait for response
    print('waiting for response')
    recorder = Recorder('request.wav')
    recorder.record_to_file()
    print('transcribing')
    result = stt('request.wav')
    transcript = result['results'][0]['alternatives'][0]['transcript']
    keyPhrase = 'I want to eat '
    if keyPhrase in transcript:
        return transcript[len(keyPhrase)::]
    else:
        print('Did not say key phrase')
        return
