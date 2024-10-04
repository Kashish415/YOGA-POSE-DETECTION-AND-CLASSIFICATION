import mediapipe as mp
import numpy as np
import cv2

def inFrame(lst):
    # Check visibility of key landmarks (nose, shoulders, hips)
    if lst[0].visibility > 0.6 and lst[11].visibility > 0.6 and lst[12].visibility > 0.6 and lst[23].visibility > 0.6 and lst[24].visibility > 0.6:
        return True
    return False

cap = cv2.VideoCapture(0)

name = input("Enter the name of the Asana: ")

holistic = mp.solutions.pose
holis = holistic.Pose()
drawing = mp.solutions.drawing_utils

X = []
data_size = 0

while True:
    lst = []

    _, frm = cap.read()
    frm = cv2.flip(frm, 1)
    res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

    if res.pose_landmarks and inFrame(res.pose_landmarks.landmark):
        for i in res.pose_landmarks.landmark:
            lst.append(i.x - res.pose_landmarks.landmark[0].x)
            lst.append(i.y - res.pose_landmarks.landmark[0].y)

        X.append(lst)
        data_size += 1

        # Debugging: Display landmark visibility
        for i, landmark in enumerate(res.pose_landmarks.landmark):
            cv2.putText(frm, f'{i}: {landmark.visibility:.2f}', (10, 20 + i*20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

    else:
        cv2.putText(frm, "Make Sure Full body is visible", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)

    drawing.draw_landmarks(frm, res.pose_landmarks, holistic.POSE_CONNECTIONS)
    cv2.putText(frm, str(data_size), (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
    cv2.imshow("window", frm)

    if cv2.waitKey(1) == 27 or data_size > 80:
        cv2.destroyAllWindows()
        cap.release()
        break

np.save(f"{name}.npy", np.array(X))
print(f"Data saved: {np.array(X).shape}")
