import sys
sys.path.insert(0, './')
import database
import emailer
import face_helper


students = database.retrieveAllStudents()
face_encoding = face_helper.getFaceEncoding('../ui/non_mask_images/aamir1.jpg')

subject = "Health department NIT Hamirpur"
body = """This is mail to inform you that you were detected without mask in Library area 
 please insure  that next time you wear a mask so you always protected from coronavirus"""
for student in students:
    print(student["face_encoding"])
    print(face_encoding)
    result = face_helper.compareFaces([student["face_encoding"]], face_encoding)
    if (result):
        print(student["name"])
        emailer.sendMailToNonMaskPerson(student["email"], subject, "Mr " + student["name"] + ", " + body)
        print("mail sent successfully")
