import faceTest
import yelp_search
import processSpeech
from face import show_webcam
'''

This is the main function that will spin up the Watson thread we developed.
OpenCV will be integrated to recognize the face of the user.

'''


def main():
    show_webcam()
    name = faceTest.run()
    processSpeech.processSpeech(name)



main()
