import pickle
import mysql.connector


def connectToMysql():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="mask_detection",
        auth_plugin='mysql_native_password',
        password="12345678",
    )
    return mydb

# face encoding example
# face_encoding = [-0.07072051,  0.08932902,  0.05445602, -0.03889629, -0.06008025,
#        -0.08600219, -0.04200263, -0.10633636,  0.15628493, -0.06203151,
#         0.22468479,  0.03042293, -0.20237291, -0.13961756,  0.03270961,
#         0.1140622 , -0.1405668 , -0.17679816,  0.00704731, -0.06050049,
#         0.00627789,  0.01387215,  0.02548384,  0.0467749 , -0.1862368 ,
#        -0.38859403, -0.09770305, -0.13771929, -0.02654994, -0.0555286 ,
#         0.05511261,  0.08895841, -0.19633052, -0.04451039,  0.04399417,
#         0.07043178, -0.05412717, -0.04304869,  0.1908658 ,  0.0627526 ,
#        -0.14659779, -0.07057554,  0.01018178,  0.24248323,  0.072477  ,
#         0.00527982,  0.09431843, -0.06806353,  0.05313507, -0.19187304,
#         0.08317781,  0.15678501,  0.1014425 ,  0.02981192,  0.07649429,
#        -0.12989642,  0.01756853,  0.11275941, -0.30249751,  0.06700344,
#         0.02327627, -0.04210065, -0.13704759, -0.03279325,  0.23785205,
#         0.20056249, -0.0794655 , -0.11014704,  0.26621458, -0.11428019,
#        -0.07138845,  0.04364203, -0.08860748, -0.21219587, -0.21027337,
#         0.04482332,  0.29068062,  0.12780881, -0.19787192,  0.01050159,
#        -0.07795351, -0.0058792 ,  0.01365038,  0.01676956, -0.09776455,
#         0.03901778, -0.06309161,  0.04304634,  0.14364651,  0.03323208,
#        -0.03435263,  0.19712722, -0.0145373 ,  0.01040277,  0.09133184,
#        -0.01390786, -0.08168637, -0.00506445, -0.16818061, -0.07670078,
#         0.09765063, -0.06657048, -0.00457288,  0.11004697, -0.15928113,
#         0.12315379,  0.02038684, -0.09918865, -0.00352135,  0.04181305,
#        -0.11108607, -0.09625246,  0.1383248 , -0.21778527,  0.25922081,
#         0.12448627,  0.00329829,  0.17049889,  0.03850527,  0.0502282 ,
#        -0.03094809, -0.14173886, -0.15319099, -0.07572862,  0.07244147,
#        -0.02389411,  0.03371891, -0.00808523]


def saveStudentInfo(name, rollno, face_encoding, email, phone):
    mydb = connectToMysql()
    mycursor = mydb.cursor()
    face_pickled_data = pickle.dumps(face_encoding)
    sql = "INSERT INTO known_students (name, rollno, face_encoding, email, phone) VALUES (%s, %s, %s , %s, %s)"
    val = (name, rollno, face_encoding, email, phone)
    mycursor.execute(sql, val)
    mydb.commit()

# retrieve data from database

def retrieveAllStudents():
    mydb = connectToMysql()
    mycursor = mydb.cursor()
    students = []

    mycursor.execute("SELECT * FROM known_students")

    myresult = mycursor.fetchall()  

    for each in myresult:
        #save to student list as dictionary
        students.append({
           "name": each[0],
           "rollno" : each[1],
           "face_encoding" : pickle.loads(each[2]), 
           "email" : each[3],
           "phone" : each[4]
        })

    return students

def retrieveStudentFromRollNo(rollno):
    mydb = connectToMysql()
    mycursor = mydb.cursor()
    student = []

    mycursor.execute(f"SELECT * FROM known_students where rollno={rollno}")

    myresult = mycursor.fetchall()  

    for each in myresult:
        #save to student list as dictionary
        student.append({
           "name": each[0],
           "rollno" : each[1],
           "face_encoding" : pickle.loads(each[2]), 
           "email" : each[3],
           "phone" : each[4]
        })

    return student





