
import cv2


cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

#make sure 'haarcascade_frontalface_default.xml' is in the same folder as this code
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id (must enter number start from 1, this is the lable of person 1)
face_id = input('\n enter id, press <enter> ==>  ')

user = input('\n enter name, press <enter> ==>  ')

face_count = int(input('\n enter no of pictures, press <enter> ==>  '))

print("\n Initializing face capture. Say Cheeeesseee ")
# Initialize individual sampling face count
count = 0

#starting face detection and getting data 
while(True):

    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    #rect(x,y,w,h)
    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/" + str(face_id) + '.' +str(user) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for stopping
    if k == 27:
        break
    elif count >= face_count: # stopping after pictures are collected
         break

# Do a bit of cleanup
print("\n  Exiting Program")
cam.release()
cv2.destroyAllWindows()