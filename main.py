# import face_recognition
# import cv2
# import math
# import os, sys
# import numpy as np  #library used for working with arrays
# import self as self



print('Hi, Mediii here')


#OpenCV-Python is a library of Python bindings designed to solve computer vision problems.
import cv2


# https://github.com/opencv/opencv/tree/4.x/data/haarcascades
# load trained xml classifiers
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

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

	for (x,y,w,h) in faces:
		# To draw a rectangle in a face
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]

	# Display an image in a window
	cv2.imshow('img',img)

	# Wait for Esc key to stop
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()

#
# def face_confidence(face_distance, face_match_threshold=0.6):
#     range = (1.0 - face_match_threshold)
#     linear_val = (1.0 - face_distance) / (range * 2.0)
#
#     if face_distance > face_match_threshold:
#         return str(round(linear_val * 100, 2)) + '%'
#     else:
#         value = (linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))) * 100
#         return str(round(value, 2)) + '%'
#
#
# class FaceRecognition:
#     face_locations = []
#     face_encodings = []
#     face_names = []
#     known_face_encodings = []
#     known_face_names = []
#     process_current_frame = True
#
#     def __init__(self):
#         self.encode_faces()
#
#     def encode_faces(self):
#         print(os.listdir())
#         for image in os.listdir('faces'):
#             face_image = face_recognition.load_image_file(f"faces/{image}")
#             face_encoding = face_recognition.face_encodings(face_image)[0]
#
#             self.known_face_encodings.append(face_encoding)
#             self.known_face_names.append(image)
#         print(self.known_face_names)
#
#     def run_recognition(self):
#         while True:
#             video_capture = cv2.VideoCapture(0)
#             # ret, frame = video_capture.read()
#             # cv2.imshow('Face Recognition', frame)
#             # # Hit 'q' on the keyboard to quit!
#             # if cv2.waitKey(1) == ord('q'):
#             #  break
#             ret, frame = video_capture.read()
#
#             # Only process every other frame of video to save time
#             if 1: #self.process_current_frame:
#                 # Resize frame of video to 1/4 size for faster face recognition processing
#                 small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#
#                 # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
#                 rgb_small_frame = small_frame[:, :, ::-1]
#
#                 # Find all the faces and face encodings in the current frame of video
#                 self.face_locations = face_recognition.face_locations(rgb_small_frame)
#                 self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)
#
#                 self.face_names = []
#                 for face_encoding in self.face_encodings:
#                     # See if the face is a match for the known face(s)
#                     matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
#                     name = "Unknown"
#                     confidence = '???'
#
#                     # Calculate the shortest distance to face
#                     face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
#
#                     best_match_index = np.argmin(face_distances)
#                     if matches[best_match_index]:
#                         name = self.known_face_names[best_match_index]
#                         #confidence = face_confidence(face_distances[best_match_index])
#                         confidence = "80%"
#
#                     self.face_names.append(f'{name} ({confidence})')
#
#             #self.process_current_frame = not self.process_current_frame
#
#             # Display the results
#             for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
#                 # Scale back up face locations since the frame we detected in was scaled to 1/4 size
#                 top *= 4
#                 right *= 4
#                 bottom *= 4
#                 left *= 4
#
#                 # Create the frame with the name
#                 cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#                 cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#                 cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)
#
#             # Display the resulting image
#             cv2.imshow('Face Recognition', frame)
#
#             # Hit 'q' on the keyboard to quit!
#             if cv2.waitKey(1) == ord('q'):
#                 break
#
#
#
# fr = FaceRecognition()
# fr.run_recognition()