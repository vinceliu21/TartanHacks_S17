import faceTest
import yelp_search
import processSpeech


name = faceTest.run()
food = processSpeech.processSpeech(name)
yelp_search.searchFood(food)
