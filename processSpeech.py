from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1


def processSpeech(name):
    '''
    Asks name what they want to do and processes
    the speech into text.

    @param name  string of name from face recognition
    @return      extracted keyword from speech
    '''
    text_to_speech = TextToSpeechV1(
        username='573eea08-b036-476e-8701-ba6afe44e12a',
        password='5qir686Ar1sz',
        x_watson_learning_opt_out=True)

    with open(join(dirname(__file__), 'resources/greeting.wav'),
              'wb') as audio_file:
        audio_file.write(
            text_to_speech.synthesize('Hello ' + name + '. \
                                      What can I do for you today?',
                                      accept='audio/wav',
                                      voice='en-US_AllisonVoice'))


processSpeech('michelle')
