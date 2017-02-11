import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

test_url = 'https://www.ibm.com/ibm/ginni/images' \
           '/ginni_bio_780x981_v4_03162016.jpg'

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='aa3972acdbfb2a4df1cbbab7aaab2686755da530')


# with open(join(dirname(__file__), '../resources/car.jpg'), 'rb') as image_file:
#     print(json.dumps(
#         visual_recognition.classify(images_file=image_file, threshold=0.1,
#                                     classifier_ids=['CarsvsTrucks_1479118188',
#                                                     'default']), indent=2))


# print(json.dumps(visual_recognition.classify(images_url=test_url), indent=2))

print(
    json.dumps(visual_recognition.detect_faces(images_url=test_url), indent=2))

# print(json.dumps(visual_recognition.list_classifiers(), indent=2))

# with open(join(dirname(__file__), '../resources/text.png'), 'rb')\
#         as image_file:
#     print(json.dumps(visual_recognition.recognize_text(images_file=image_file),
#                      indent=2))

# with open(join(dirname(__file__), '../resources/face.jpg'), 'rb')\
#         as image_file:
#     print(json.dumps(visual_recognition.detect_faces(images_file=image_file),
#                      indent=2))