import face_recognition
import urllib.request

# imageTrue = face_recognition.load_image_file('./images/known/rock_gym.jpg')
response = urllib.request.urlopen("https://raw.githubusercontent.com/WebDevSimplified/Face-Recognition-JavaScript/master/labeled_images/Hawkeye/1.jpg")
imageTrue = face_recognition.load_image_file(response)
imageEncoding = face_recognition.face_encodings(imageTrue)[0]

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
  },
]
for obj in arrayOfObj:
  print(obj['img'])
  testResponse = urllib.request.urlopen(obj['img'])
  imageTest = face_recognition.load_image_file(testResponse)

  # newImage = face_recognition.load_image_file(
  #     './images/unknown/youngrock.jpg')
  newImageEncoding = face_recognition.face_encodings(imageTest)[0]

  # Compare faces
  results = face_recognition.compare_faces(
      [imageEncoding], newImageEncoding)

  if results[0]:
      obj['verified'] = 1
  else:
      print('This is NOT Bill Gates', results)
print(arrayOfObj)