import cv2

img_file = "car_img.jpg"  #Car Image to test
video = cv2.VideoCapture("Pedestrians_Compilation.mp4")
video.get(3)


#img = cv2.imread(img_file)  #Create OpenCV image which reads all the pixels data of img_file and stores it in some multidimensional array with every pixel has its own data

#Pretrained calssifier with Haar features which captures how a car should look in an image
classifier_file_car = 'car_detector.xml'  
classifier_file_pedestrian = 'ped_detector.xml'

#Classifier
car_tracker = cv2.CascadeClassifier(classifier_file_car)
ped_tracker = cv2.CascadeClassifier(classifier_file_pedestrian)

#read all frame till the car stops or video is over
while True:
    
    #video.read() return a tuple with first part as if the read was successful and second the frame
    read_successful,frame = video.read()  #reading current frame 
  #  print(read_successful)
    if read_successful:
        grayscale_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    else:
        break
    
    #Detect cars of any scale(size) and detected img are returned as a list of rectangles
    cars = car_tracker.detectMultiScale(grayscale_frame) 
    pedestrian = ped_tracker.detectMultiScale(grayscale_frame)

    #print(cars)
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)  #Draw rectangle around pedestrians
        
    for (x,y,w,h) in pedestrian:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)  #Draw rectangle around pedestrians
        


    cv2.imshow("Object detector",frame)
    
    key = cv2.waitKey(1)

    if key == 81 or key == 113:  #Stop is Q key is pressed
        break

#release video captured
video.release()

print("Project Complelted")