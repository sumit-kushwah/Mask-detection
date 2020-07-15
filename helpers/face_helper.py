import face_recognition

def getFaceEncodings(imagePath):
    image = face_recognition.load_image_file(imagePath)
    return face_recognition.face_encodings(image)

def compareFaces(knownFaceEncodings, encoding_to_check):
        return face_recognition.compare_faces(knownFaceEncodings, encoding_to_check)

def getFaceEncoding(singleImagePath):
    image = face_recognition.load_image_file(singleImagePath)
    return face_recognition.face_encodings(image)[0]
