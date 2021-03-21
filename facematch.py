import face_recognition
import urllib.request

# imageTrue = face_recognition.load_image_file('./images/known/rock_gym.jpg')
response = urllib.request.urlopen("https://raw.githubusercontent.com/WebDevSimplified/Face-Recognition-JavaScript/master/labeled_images/Hawkeye/1.jpg")
imageTrue = face_recognition.load_image_file(response)
imageEncoding = face_recognition.face_encodings(imageTrue)[0]

testResponse = urllib.request.urlopen("https://raw.githubusercontent.com/WebDevSimplified/Face-Recognition-JavaScript/master/labeled_images/Hawkeye/1.jpg")
imageTest = face_recognition.load_image_file(testResponse)



# newImage = face_recognition.load_image_file(
#     './images/unknown/youngrock.jpg')
newImageEncoding = face_recognition.face_encodings(imageTest)[0]

# Compare faces
results = face_recognition.compare_faces(
    [imageEncoding], newImageEncoding)

if results[0]:
    print(results)
else:
    print('This is NOT Bill Gates', results)