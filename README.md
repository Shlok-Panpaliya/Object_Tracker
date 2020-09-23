
# Object_Tracker
A realtime car and pedestrain detection using OpenCV and Python.</br>
Haar Feature-based Cascade Classifier for Object Detection has been used.

#### OpenCV Documentation
https://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html?highlight=detectmultiscale

#### Understanding Haar-Feature based Cascade Classifer
http://www.willberger.org/cascade-haar-explained/

### Feature of the app
- Detects cars and pedestrian with Haar Cascade Classifier in Real time and makes rectangle around detected object.

## Initial Setup
##### make a new folder
```
mkdir object_tracker
```
##### Setup a virtual enviornment
```
python3 -m venv venv
source venv/bin/activate
```
##### Download the files in the repository
##### Install OpenCV
```
pip install opencv-python
```
##### Running the app
```
python object_tracker.py
```
### Example Output frame

![Screenshot from 2020-09-21 10-39-02](https://user-images.githubusercontent.com/43007503/93735664-5898e680-fbfb-11ea-8db3-a685a03af8a0.png)

![Screenshot from 2020-09-21 10-40-59](https://user-images.githubusercontent.com/43007503/93735692-71090100-fbfb-11ea-993c-96899eccc33a.png)
