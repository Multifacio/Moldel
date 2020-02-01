from FaceVisibilityLayers.Configuration import FACE_IMAGE_LOCATIONS, EPISODE_VIDEO_LOCATION, FRAME_SKIP, IDENTIFIER_NAME
import face_recognition as fr
import cv2

class FaceTracker:
    """ The FaceTracker determines how often a face of a candidate is visible during an episode. This code is based
    on the project of mattijn: https://github.com/mattijn/widm
    Update the configuration file manually before running this code and store the result in the Data file (which will
    be used by the Face Visibility Layer). """

    # Setting the tolerance higher means that faces get detected more earlier
    TOLERANCE = 0.50

    def track_faces(self):
        print(IDENTIFIER_NAME)
        all_candidates = list(FACE_IMAGE_LOCATIONS.keys())
        score = dict()
        for candidate in all_candidates:
            score[candidate] = 0

        # Load the face images of all candidates
        known_faces = []
        for candidate in all_candidates:
            image = fr.load_image_file(FACE_IMAGE_LOCATIONS[candidate])
            known_faces.append(fr.face_encodings(image)[0])

        # Read the frames of the episode
        video_capture = cv2.VideoCapture(EPISODE_VIDEO_LOCATION)
        length = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_count = 0
        while video_capture.isOpened():
            continues, frame = video_capture.read()
            if not continues: # If this is the last frame then stop
                video_capture.release()
                break
            frame_count += 1
            if frame_count % 500 == 0: # Show progress every 500 frames
                print('{}/{}'.format(frame_count, length))
            if frame_count % FRAME_SKIP == 0: # Only analyse every FRAME_SKIP frame
                # Find all faces in this frame
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                rgb_frame = frame[:, :, ::-1]
                face_locations = fr.face_locations(rgb_frame)
                found_faces = fr.face_encodings(rgb_frame, face_locations)
                for ff in found_faces:
                    # Check which candidate face matches with the founded face
                    match = fr.compare_faces(known_faces, ff, tolerance = self.TOLERANCE)
                    for i, candidate in enumerate(all_candidates):
                        if match[i]:
                            score[candidate] += 1
                            break

        # Print the score
        print(IDENTIFIER_NAME)
        print(score)

ft = FaceTracker()
ft.track_faces()
