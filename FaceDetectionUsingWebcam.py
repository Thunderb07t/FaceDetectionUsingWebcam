#First Copy the 'haarcascade_frontalface_default.xml' file from the 'Python' folder to the location where the program is stored.
import cv2

camera=cv2.VideoCapture(0)
#Starts Camera Capturing of camera Of index 0.that is our webcam in this condition
while 1:
    ret,img=camera.read() 
    #ret stores true or false which states whether image is captured or not
    #img stores image data captured from webcam

    #Load the haar cascade
    faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #Filename with extension in quotes

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#Converting the Colored image to Gray

    faces=faceCascade.detectMultiScale(gray,1.3,5)#Detect several no and sizes of faces

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #To draw the rectangle around the face

    cv2.imshow('img',img) #Displays the image

    #To exit press Esc key
    k = cv2.waitKey(30) #Waits for the pressed key
    if k == 27:
        break
    
camera.release() #Releases the WebCam
cv2.destroyAllWindows() #Destroys all of the windows
