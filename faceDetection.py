import cv2  # OpenCV-Python is a library of Python bindings designed to solve computer vision problems.

print('Hi, Mediii here')
print('This is the file that works only for DETECTION of the face')

# https://github.com/opencv/opencv/tree/4.x/data/haarcascades
# Haar Cascade is basically a classifier which is used to detect the objects for which it has been trained for, from the source.
# load trained xml classifiers
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# face_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
#
# capture frames from a camera
cap = cv2.VideoCapture(0)

# loop runs if capturing has been initialized.
while 1:

    # reads frames from a camera
    ret, img = cap.read()

    # convert to gray scale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detects faces of different sizes in the input image
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)

    for (x, y, w, h) in faces:
        # To draw a rectangle in a face
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

    # Display an image in a window
    cv2.imshow('img', img)

    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xff
    if k == 27:
        break

# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()

