import face_recognition
import cv2  # OpenCV-Python is a library of Python bindings designed to solve computer vision problems.
import os
import numpy as np  # library used for working with arrays
import self as self

print('Hi, Mediii here')
print('This program is for RECOGNITION of the faces')


class FaceRecognition:
    face_locations = []
    face_encodings = []
    face_names = []
    known_face_encodings = []
    known_face_names = []
    process_current_frame = True

    def __init__(self):
        self.encode_known_faces()

    def encode_known_faces(self):
        # loop trough faces folder for every image
        for image in os.listdir('faces'):
            face_image = face_recognition.load_image_file(f"faces/{image}")
            face_encoding = face_recognition.face_encodings(face_image)[0]
            # print(face_encoding)
            self.known_face_encodings.append(face_encoding)
            self.known_face_names.append(image)
        print('known faces')
        print(self.known_face_names)

    # video
    def run_recognition(self):
        while True:
            video_capture = cv2.VideoCapture(0)
            if not video_capture.isOpened():
                print('Cannot open camera')
            ret, frame = video_capture.read()

            # Only process every other frame of video to save time
            if self.process_current_frame:
                self.face_locations = face_recognition.face_locations(frame)
                # print('we found faces')
                # print(self.face_locations)
                self.face_encodings = face_recognition.face_encodings(frame, self.face_locations)
                # print('face encodings are')
                # print(self.face_encodings)
                self.face_names = []
                for face_encoding in self.face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = "Unknown"

                    # Calculate the shortest distance to face
                    face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)

                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]
                    self.face_names.append(f'{name.split(".")[0]}')

            self.process_current_frame = not self.process_current_frame

            # Display the results
            for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                # Create the frame with the name
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)

            # Display the resulting image
            cv2.imshow('Face Recognition', frame)

            # Wait for Esc key to stop
            k = cv2.waitKey(5) & 0xff
            if k == 27:
                break


fr = FaceRecognition()
fr.run_recognition()
