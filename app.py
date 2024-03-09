import cv2
import numpy as np
from function import *
import mediapipe as mp
from keras.utils import to_categorical
from keras.models import model_from_json
from keras.layers import LSTM, Dense
from keras.callbacks import TensorBoard

mp_hands = mp.solutions.hands

json_file = open("model.json", "r")
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)
model.load_weights("model.h5")

colors = [(245, 117, 16) for _ in range(20)]

def prob_viz(res, actions, input_frame, colors, threshold):
    output_frame = input_frame.copy()
    for num, prob in enumerate(res):
        cv2.rectangle(output_frame, (0, 60 + num * 40), (int(prob * 100), 90 + num * 40), colors[num], -1)
        cv2.putText(output_frame, actions[num], (0, 85 + num * 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,
                    cv2.LINE_AA)
    return output_frame

sequence = []
sentence = []
accuracy = []
predictions = []
threshold = 0.8

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
    while True:

        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab frame.")
            break

        image, results = mediapipe_detection(frame, hands)
        
        try:
            keypoints = extract_keypoints(results)
        except Exception as e:
            print("Error during hand detection:", e)
            keypoints = None

        # Use only the detected hand landmarks for further processing
        if keypoints is not None and keypoints.any():
            sequence.append(keypoints)
            sequence = sequence[-30:]

            try:
                if len(sequence) == 30:
                    res = model.predict(np.expand_dims(sequence, axis=0))[0]
                    print(actions[np.argmax(res)])
                    predictions.append(np.argmax(res))

                    if np.unique(predictions[-10:])[0] == np.argmax(res):
                        if res[np.argmax(res)] > threshold:
                            if len(sentence) > 0:
                                if actions[np.argmax(res)] != sentence[-1]:
                                    sentence.append(actions[np.argmax(res)])
                                    accuracy.append(str(res[np.argmax(res)] * 100))
                            else:
                                sentence.append(actions[np.argmax(res)])
                                accuracy.append(str(res[np.argmax(res)] * 100))

                    if len(sentence) > 1:
                        sentence = sentence[-1:]
                        accuracy = accuracy[-1:]

            except Exception as e:
                print("Error during model prediction:", e)

        cv2.rectangle(frame, (0, 0), (330, 40), (0, 255, 0), -1)
        cv2.putText(frame, "Output:- {} {}".format(' '.join(sentence), ' '.join(["{:.2f}%".format(float(acc)) for acc in accuracy])), (3, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('OpenCV Feed', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()