import cv2

img_file = "car_img.jpg"  #Car Image to test
video = cv2.VideoCapture("Tesla_Autopilot_Dashcam.mp4")
video.get(3)


#img = cv2.imread(img_file)  #Create OpenCV image which reads all the pixels data of img_file and stores it in some multidimensional array with every pixel has its own data

#Pretrained calssifier with Haar features which captures how a car should look in an image
classifier_file = 'car_detector.xml'  

#Car classifier
car_tracker = cv2.CascadeClassifier(classifier_file)  
#read all frame till the car stops or video is over
while True:
    
    #video.read() return a tuple with first part as if the read was successful and second the frame
    read_successful,frame = video.read()  #reading current frame 
    if read_successful:
        grayscale_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    else:
        break
    cv2.imshow("Object detector",grayscale_frame)
    cv2.waitKey(1)

"""
#converting img to grayscale as needed for HAAR feature classifier
black_n_white = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 



#Detect cars of any scale(size) and detected img are returned as a list of rectangles
cars = car_tracker.detectMultiScale(black_n_white) 

#print(cars)

for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)  #Draw rectangle around cars

#Display the img with object spotted
cv2.imshow("OBJECT_DETECTOR",img)  

#img dosent autoclose until key is pressed
cv2.waitKey(0) 
"""
print("Project Complelted")