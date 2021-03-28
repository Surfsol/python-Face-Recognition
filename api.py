import flask
from flask import Flask, request
import face_recognition
import urllib.request
from urllib.request import urlopen
import json
import skimage
from skimage import io
from PIL import Image
import urllib3
from imageio import imread

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def faceLoop(array):
  baseImg = array[0]['img']
  #"http://res.cloudinary.com/siingly/image/upload/q_auto:eco/v1616524065/6a419d8a95cda89abeb437498cd84611.png"
  # "https://wiki.d-addicts.com/images/thumb/5/5b/AngelaBaby.jpg/300px-AngelaBaby.jpg"

  baseImg = urllib.request.urlretrieve(baseImg, 'base.jpeg')
  print('111111111111111111115555 HTTPResponse', baseImg)
  #HTTPResponse <http.client.HTTPResponse object at 0x1FBC6A18>
  # with open(baseImg, 'rb') as rf:
  #   with open('base_img.jpg', 'wb') as wf:
  #     for line in rf:
  #       wf.write(line)
  #convert http response to a jpeg file
 
 
  # is encoding http response
  baseEncode = face_recognition.load_image_file("base.jpeg")
  print('3 base ', baseEncode[0])
  if(len(face_recognition.face_encodings(baseEncode)) == 0):
    return array
  base_encoding = face_recognition.face_encodings(baseEncode)[0]
  print('4 base', baseEncode)
  for obj in array:
    testImg = urllib.request.urlopen(obj['img'])
    imageTest = face_recognition.load_image_file(testImg)
    if(len(face_recognition.face_encodings(imageTest)) != 0):
      imageTest = face_recognition.face_encodings(imageTest)[0]
      print('image test',imageTest)
      # Compare faces
      results = face_recognition.compare_faces(
          [base_encoding], imageTest)
      if results[0]:
          obj['verified'] = 1
      else:
          obj['verified'] = 0
  return array


@app.route('/', methods=['GET'])
def home():
  return "<h1>Image classifier.</p>"
@app.route('/classify', methods=['POST'])
def classify_image():
  data = request.json
  print(data)
  objRes = faceLoop(data)
  return json.dumps(objRes), 200
app.run()