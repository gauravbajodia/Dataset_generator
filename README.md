# Dataset_generator
This code can be used to generate personalized data set of faces and objects for object/face recognition purposes
make sure that haarcascade_frontalface_default is in the same directory as the code.
create a folder named dataset in the same directory as the code.

# Hello every body, 
# Gaurav here.
Todays we will reviewing this revised code which can be used to make personalized data set.
Now you must be thinking that I can easily find any sort of data set on internet,
But what if you require a personalized data set? Like for example your photos for a face recognition code. It def would be creepy if you find a 100 photos of yourself on internet posted by someone.
But again the que is I have a camera or a smartphone I can click photos of myself.  But we know how much data is required to achieve a good accuracy for a model.
Are you sure you wanna sit there and click 100 of photos of yourself? You might be an essentric at that point.so without further blabbering lets get into this code.

# CODE

import cv2
//OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library.

cam = cv2.VideoCapture(0)
//cv.capture is used to initialise the web cam.
//Device index is just the number to specify which camera. Normally one camera will be connected (as in my case). So I simply pass 0 (or -1). 
//You can select the second camera by passing 1 and so on.

cam.set(3, 640) # set video width
cam.set(4, 480) # set video height
//using cam.set to set the height and width of input webcam 

#make sure 'haarcascade_frontalface_default.xml' is in the same folder as this code
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
//OpenCV's algorithm is currently using the following Haar-like features which are the input to the basic classifiers. 
//These classifiers are all pre trained.You can download different classifiers from their website or gituhub repositories 
//For this particular project we are using the haarcascade frontal face classifier

#For each person, enter one numeric face id (must enter number start from 1, this is the lable of person 1)
face_id = input('\n enter id, press <enter> ==>  ')

user = input('\n enter name, press <enter> ==>  ')

face_count = int(input('\n enter no of pictures, press <enter> ==>  '))

print("\n Initializing face capture. Say Cheeeesseee ")

#Initialize individual sampling face count
count = 0

#starting face detection and getting data 
while(True):


#Capture frame-by-frame
    ret, img = cam.read()
// read(). Basically, ret is a boolean regarding whether or not there was a return at all, at the frame is each frame that is returned. .
//cap.read() returns a bool (True/False). If frame is read correctly, it will be True
//so basically cam.read gives bool for working of webcam and ret check if bool is being received or not    
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
//this LOC simpy converts colour images to balck and white.

faces = face_detector.detectMultiScale(gray (image name) , 1.3( scale factor), 5 (min neighor))
//n neighbour=Parameter specifying how many neighbors each candidate rectangle should have to retain it. This parameter will affect the quality of the detected faces: higher //lue results in less detections but with higher quality. We're using 5 in the code.
// faces are found, it returns the positions of detected faces as Rect(x,y,w,h).
//ce we get these locations, we can create a ROI for the face and apply face detection on this ROI.

    for (x,y,w,h) in faces:

        cv2.rectangle(img,      (x,y),    (x+w,y+h), (255,0,0),   2)     
//image = cv2.rectangle(image, start_point, end_point, color,    thickness)
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/" + str(face_id) + '.' +str(user) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
                    (directory  +     id       +      name       +currenct pic count+ format
        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for stopping
    if k == 27:
        break
    elif count >= face_count: # stopping after pictures are collected
         break

#Do a bit of cleanup
print("\n Exiting Program ")
cam.release()
// to stop tthe web cam
cv2.destroyAllWindows()
// to destroy the subsidieary python window of webcam
