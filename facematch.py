import face_recognition
import urllib.request
import flask
from flask import Flask, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True




# imageTrue = face_recognition.load_image_file('./images/known/rock_gym.jpg')
# response = urllib.request.urlopen("https://raw.githubusercontent.com/WebDevSimplified/Face-Recognition-JavaScript/master/labeled_images/Hawkeye/1.jpg")
# imageTrue = face_recognition.load_image_file(response)
# imageEncoding = face_recognition.face_encodings(imageTrue)[0]

# def face (imageTest, imageEncoding):
#   newImageEncoding = face_recognition.face_encodings(imageTest)[0]

#   # Compare faces
#   results = face_recognition.compare_faces(
#       [imageEncoding], newImageEncoding)

#   if results[0]:
#       obj['verified'] = 1
#   else:
#       print('This is NOT Bill Gates', results)

 arrayOfObj = [
  {
    "img":
      "https://raw.githubusercontent.com/WebDevSimplified/Face-Recognition-JavaScript/master/labeled_images/Hawkeye/1.jpg",
    "verified": 0,
    "adult": 0
  },
  {
    "img":
      "https://raw.githubusercontent.com/WebDevSimplified/Face-Recognition-JavaScript/master/labeled_images/Thor/2.jpg",
    "verified": 0,
    "adult": 0
  },
  {
    "img":
      "https://raw.githubusercontent.com/WebDevSimplified/Face-Recognition-JavaScript/master/labeled_images/Hawkeye/1.jpg",
    "verified": 0,
    "adult": 0
  }
]

def faceLoop(array):
  baseImg = array[0]['img']
  baseImg = urllib.request.urlopen(baseImg)
  baseEncode = face_recognition.load_image_file(baseImg)
  baseEncode = face_recognition.face_encodings(baseEncode)[0]
  for obj in array:
    testImg = urllib.request.urlopen(obj['img'])
    imageTest = face_recognition.load_image_file(testImg)
    imageTest = face_recognition.face_encodings(imageTest)[0]
    # Compare faces
    results = face_recognition.compare_faces(
        [baseEncode], imageTest)

    if results[0]:
        obj['verified'] = 1
    else:
        print('This is NOT Bill Gates', results)
  return array

faceLoop(arrayOfObj)  

  # newImage = face_recognition.load_image_file(
  #     './images/unknown/youngrock.jpg')

@app.route('/', methods=['GET'])
def home():
  print('in home')
  return "<h1>Image classifier.</p>"
@app.route('/classify', methods=['POST'])
def classify_image():
  print('in classifier')
  data = request.form
  print(data)

app.run()


arrayOfObj = [
  {
    "img":
      "https://api.tinify.com/output/1y0gfawpcfrrz2129uw6k8kme88pbr85",
    "verified": 0,
    "adult": 0
  },
  {
    "img":
      "https://api.tinify.com/output/utkmgfk3r88a3dktjnf81crp0faa2pj0",
    "verified": 0,
    "adult": 0
  },
  {
    "img":
      "https://api.tinify.com/output/3de9u8hghghqfmtp96b27rm08y1mkeg6",
    "verified": 0,
    "adult": 0
  },
   {
    "img":
      "https://api.tinify.com/output/czyp4hz9j341wqjcxfcnb3ygtecay45k",
    "verified": 0,
    "adult": 0
  }
]

{"http://res.cloudinary.com/siingly/image/upload/q_auto:eco/v1616524065/6a419d8a95cda89abeb437498cd84611.png"}