import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
from face import show_webcam
test_url = 'http://www.talentedprofiles.com/wp-content/uploads/2016/10/25906514-600x600_t.png'

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='aa3972acdbfb2a4df1cbbab7aaab2686755da530')

show_webcam()
#print(json.dumps(visual_recognition.create_collection("testcollect"), indent=2))
# with open(join(dirname(__file__), '../FullSizeRender.jpg'), 'rb')\
#             as image_file:
#             print(json.dumps(visual_recognition.add_image("testcollect_baf4a0", image_file, {'name' : 'Johnny Wu'}), indent = 2))

ok = input("Please input your name")

print("The image added should be in the resources folder")
with open(join(dirname(__file__), '../TartanHacks_S17/resources/vince.png'), 'rb') as image_file:
    print(json.dumps(visual_recognition.add_image("testcollect_baf4a0", image_file, {'name' : ok}), indent = 2))
