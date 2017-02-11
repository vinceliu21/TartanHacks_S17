from AudioFile import AudioFile
from recorder import Recorder
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
from watson_developer_cloud import SpeechToTextV1
from budget_watson import watson_budget
import yelp_search
import datetime


def tts(text, filename):
    text_to_speech = TextToSpeechV1(
        username='573eea08-b036-476e-8701-ba6afe44e12a',
        password='5qir686Ar1sz',
        x_watson_learning_opt_out=True)

    #  Initial greeting
    with open(join(dirname(__file__), filename),
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
    if "Cho" in name:
        name = "Edward"
    elif "Wu" in name:
        name = "Johnny"
    elif "Deng" in name:
        name = "Michelle"
    elif "Liu" in name:
        name = "Vincent"
    #  Initial greeting
    tts('Hello ' + name + '. \
        What can I do for you today?', 'resources/greeting.wav')
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

    if (datetime.datetime.time(datetime.datetime.now()) > datetime.time(4, 20, 0, 0) and
            datetime.datetime.time(datetime.datetime.now()) < datetime.time(4, 20, 59, 0)):
        tts("ayy lmao", 'resources/420.wav')
        audio = AudioFile('resources/420.wav')
        audio.play()
        audio.close()

    # Eating Section
    if "eat" in transcript:

        keyPhrase = 'I want to eat '
        if keyPhrase in transcript:
            yelp_search.searchFood(transcript[len(keyPhrase)::])
            return processSpeech(name)
        else:
            print('Did not say key phrase')
            return processSpeech(name)

    # Budget Section
    elif "budget" in transcript:
        watson_budget("Edward", "Friday")
        return processSpeech(name)

    elif "time" in transcript:
        tts("The current time is " +
            datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"),
            'resources/time.wav')
        audio = AudioFile('resources/time.wav')
        audio.play()
        audio.close()
    # Default Case for not getting any proper key words
    else:
        return processSpeech(name)
