import cv2

img_file = "car_img.jpg"  #Car Image to test

img = cv2.imread(img_file)  #Create OpenCV image which reads all the pixels data of img_file and stores it in some multidimensional array with every pixel has its own data

classifier_file = 'car_detector.xml'  #Pretrained calssifier with Haar features which captures how a car should look in an image

black_n_white = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting img to grayscale as needed for HAAR feature classifier

car_tracker = cv2.CascadeClassifier(classifier_file) #Car classifier 

cars = car_tracker.detectMultiScale(black_n_white) #Detect cars of any scale(size) and detected img are returned as a list of rectangles

#print(cars)

for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)  #Draw rectangle around cars

cv2.imshow("OBJECT_DETECTOR",black_n_white)  #Display the img with object spotted

cv2.waitKey(0) #img dosent autoclose until key is pressed

print("Project Complelted")