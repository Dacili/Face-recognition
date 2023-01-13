# Face detection and face recognition

So what is the difference?  
![image](https://user-images.githubusercontent.com/37112852/212126082-1725ac96-d609-40d6-ba78-1384afa2ed7a.png)  
Detection only detect faces, while recognition is actually face detection + face identification.    

There are two files in this project:
1. faceDetection.py
2. faceRecognition.py  
Names are selfexplanatory haha.  <br>

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
Note: I had a lot of issues when trying to install **dlib** library which was needed for face-recognition pkg.  
I succeeded to install it with this stackoverflow answer: https://stackoverflow.com/questions/74476152/error-in-installing-dlib-library-in-python3-11/74573179#74573179   
Github repo for classifiers, used in faceDetection.py:  https://github.com/opencv/opencv/tree/4.x/data/haarcascades
<br>
### Face detection   
<img width="610" alt="face detection" src="https://user-images.githubusercontent.com/37112852/212325912-4077b809-248a-4cbb-8892-864130c07f01.PNG">  
<br>
### Face recognition demo



https://user-images.githubusercontent.com/37112852/212326325-ce4f53ec-0ac4-499b-b0e0-c0c9d3900af2.mp4







