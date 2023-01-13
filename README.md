# Face detection and face recognition

So what is the difference?  
![image](https://user-images.githubusercontent.com/37112852/212126082-1725ac96-d609-40d6-ba78-1384afa2ed7a.png)  
Detection only detect faces, while recognition is actually face detection + face identification.    

There are two files in this project:
1. faceDetection.py
2. faceRecognition.py  
Names are selfexplanatory haha. In order to exit the scripts press Esc. <br>

### Face detection    
Firstly we have to use some classifier (Github repo for **classifiers**, used in faceDetection.py:  https://github.com/opencv/opencv/tree/4.x/data/haarcascades) in order to train the opencv object. After that we're using the camera, and analyzing the frames in order to find the objects for which we used the classifiers. Once objects are detected on the image, show the image.   
<img width="610" alt="face detection" src="https://user-images.githubusercontent.com/37112852/212325912-4077b809-248a-4cbb-8892-864130c07f01.PNG">  
   
### Face recognition demo  
Folder faces, acts like a "database" for known faces. There we put images of known faces, where name of the image, is the name of the person. At the beginning of the script we're performing encoding (128-dimension face encoding for each face in the image) for known faces.  
After that, we're using the camera, and analyzing the frames, in order to detect faces. Once faces are detected, we're also encoding that image, and after that trying to find a match with our known faces. If match happens, the name is shown on the image, otherwise Unknown is shown.  



https://user-images.githubusercontent.com/37112852/212326325-ce4f53ec-0ac4-499b-b0e0-c0c9d3900af2.mp4

  
**Specifications:**  
Python version:  3.11.1   
pip 22.3.1    
opencv-python==4.7.0.68  
dlib==19.24.99  
face-recognition==1.3.0  

<br> 
  
In packagesFile.txt there are all packages versions info. To get that I run:  
```  
pip freeze > packagesFile.tx
```  
To install these packages when pulling the code run:  
```  
pip install -r packagesFile.tx
```  
Note: I had a lot of issues when trying to install **dlib** (a toolkit for making real world machine learning and data analysis applications) library which was needed for face-recognition pkg.  
I succeeded to install it with this stackoverflow answer: https://stackoverflow.com/questions/74476152/error-in-installing-dlib-library-in-python3-11/74573179#74573179   

<br>




