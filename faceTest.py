import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

test_url = 'http://www.talentedprofiles.com/wp-content/uploads/2016/10/25906514-600x600_t.png'

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='aa3972acdbfb2a4df1cbbab7aaab2686755da530')

#print(json.dumps(visual_recognition.create_collection("testcollect"), indent=2))
# with open(join(dirname(__file__), '../FullSizeRender.jpg'), 'rb')\
#             as image_file:
#             print(json.dumps(visual_recognition.add_image("testcollect_baf4a0", image_file, {'name' : 'Johnny Wu'}), indent = 2))

input_var = input("Would you like to add an image or match an image? Enter A for add or M for match: ")
if input_var == "A":
    print("The image added should be in the location one folder higher than the location of this program")
    input_var2 = input("Enter the image filename, along with file extension: ")
    input_var3 = input("Enter the name of the subject: ")
    with open(join(dirname(__file__), '../' + input_var2), 'rb')\
             as image_file:
             print(json.dumps(visual_recognition.add_image("testcollect_baf4a0", image_file, {'name' : input_var3}), indent = 2))
elif input_var == "M":
    input_var4 = input("Enter the image filename you would like to match, along with its extension: ")
    with open(join(dirname(__file__), '../' + input_var4), 'rb')\
              as image_file:
              rJson = json.dumps(visual_recognition.find_similar("testcollect_baf4a0", image_file, limit = 1), indent = 2)
              jsonObj = json.loads(rJson)
              for x in jsonObj["similar_images"]:
                print("Hello " + x["metadata"]["name"])

# print(json.dumps(visual_recognition.list_images("testcollect_a3c24f"), indent = 2))

# with open(join(dirname(__file__), '../IMG_2791.JPG'), 'rb')\
#              as image_file:
#              print(json.dumps(visual_recognition.find_similar("testcollect_baf4a0", image_file, limit = 1), indent = 2))


# with open(join(dirname(__file__), '../resources/car.jpg'), 'rb') as image_file:
#     print(json.dumps(
#         visual_recognition.classify(images_file=image_file, threshold=0.1,
#                                     classifier_ids=['CarsvsTrucks_1479118188',
#                                                     'default']), indent=2))


# print(json.dumps(visual_recognition.classify(images_url=test_url), indent=2))

# print(
#     json.dumps(visual_recognition.detect_faces(images_url=test_url), indent=2))

# print(json.dumps(visual_recognition.list_classifiers(), indent=2))

# with open(join(dirname(__file__), '../resources/text.png'), 'rb')\
#         as image_file:
#     print(json.dumps(visual_recognition.recognize_text(images_file=image_file),
#                      indent=2))

# with open(join(dirname(__file__), '../FullSizeRender.jpg'), 'rb')\
#         as image_file:
#     print(json.dumps(visual_recognition.detect_faces(images_file=image_file),
#                      indent=2))