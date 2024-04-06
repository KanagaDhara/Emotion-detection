import cv2
import numpy as np
from keras.models import model_from_json

emotion_dict={0:'Angry', 1:'Disgusted', 2:'Fearful',3:'Happy',4:'Neutral',5:'Sad',6:'Suprised'}

#load json and create model

json_file=open(r'C:\Users\admin\Documents\data science\Projects\Emotion Detection\Video&images\model_a1.json','r')
loaded_model_json = json_file.read()
json_file.close()
emotion_model = model_from_json(loaded_model_json)

#load weights into new model
emotion_model.load_weights(r'C:\Users\admin\Documents\data science\Projects\Emotion Detection\Video&images\model1.weights.h5')
print('loaded model from disk')

#start the webcam feeed
cap= cv2.VideoCapture(0)

#cap=cv2.VideoCapture(r"C:\Users\admin\Documents\data science\Projects\Emotion Detection\Video&images\Sample videos\emotion_video_sample1.mp4")

while True:
    #Find haarcascade to draw bounding box around face
    ret,frame = cap.read()
    frame = cv2.resize(frame,(1000,720))
    if not ret:
        print("Error: Failed to capture frame.")
        break
    face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #detect faces available on camera
    num_faces = face_cascade.detectMultiScale(gray_frame, scaleFactor = 1.3, minNeighbors = 5)

    #take each face available on camera and Preprocess it
    for (x,y,w,h) in num_faces:
        cv2.rectangle(frame,(x,y-50),(x+w,y+h+10),(0,255,0),4)
        roi_gray_frame = gray_frame[y:y + h,x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame,(48,48)),-1),0)
        #predict the emotion
        emotion_prediction = emotion_model.predict(cropped_img)
        maxindex = int(np.argmax(emotion_prediction))
        cv2.putText(frame, emotion_dict[maxindex], (x+5, y-20), cv2.FONT_HERSHEY_SIMPLEX,1, (255,0,0),2,cv2.LINE_8)

    cv2.imshow('Emotion Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
