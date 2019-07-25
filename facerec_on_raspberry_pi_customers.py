import face_recognition
import picamera
import numpy as np
import os
import time
import json
from confluent_kafka import Producer

#初始化
camera = picamera.PiCamera()
#設置相機解析度
camera.resolution = (320, 240)

output = np.empty((240, 320, 3), dtype=np.uint8)


print("Loading known face image(s)")


face_locations = []
face_encodings = []
face_names = []

known_person=[]
known_image=[]
known_face_encoding=[]


# 創建一個名為"customers"資料夾並從裡面的會員人臉抓取人臉特徵並以檔案名稱為人臉名稱
for file in os.listdir("customers"):
    try:
        known_person.append(file.replace(".jpg", ""))
        file=os.path.join("customers/", file)
        known_image = face_recognition.load_image_file(file)
        known_face_encoding.append(face_recognition.face_encodings(known_image)[0])
    except Exception as e:
        pass



while True:
    print("Capturing image.")
    #從相機抓取一幀圖像轉為numpy陣列
    camera.capture(output, format="rgb")

    # 找出當前視頻中所有的人臉及臉部編碼
    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)

    # 循環檢查框架中的人臉是否為已知的會員人臉
    for face_encoding in face_encodings:
        props={'bootstrap.servers':'10.120.28.3:6667'}
        p = Producer(props)
        match = face_recognition.compare_faces(known_face_encoding, face_encoding, tolerance=0.45)
        matches=np.where(match)[0] #檢查哪個圖片是符合的
        if len(matches)>0:
          name = str(known_person[matches[0]])
          member_detail = {"memberID" : name} 
          member_detail_json = json.dumps(member_detail).encode("utf-8") 
          p.produce('facein', value=member_detail_json)
        else:
          name = "Unknown"

        print("I see someone named {}!".format(name), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))




