import cv2
import mediapipe as mp
import serial
import time

# Initialize Serial Communication (Change COM port as per your system)
arduino = serial.Serial(port="COM5", baudrate=9600, timeout=1)  # Change COM5 if needed
time.sleep(2)  # Wait for Arduino to initialize

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Function to check finger status
def count_fingers(hand_landmarks):
    finger_tips = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky fingertips
    raised = []

    for tip in finger_tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            raised.append(tip)

    thumb_tip = 4
    thumb_base = 2
    if hand_landmarks.landmark[thumb_tip].x < hand_landmarks.landmark[thumb_base].x:
        raised.append(thumb_tip)

    return len(raised)

# OpenCV Video Capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw Green Hand Landmarks
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)
            )

            fingers = count_fingers(hand_landmarks)

            # Send commands to Arduino via Serial
            if fingers == 5:
                arduino.write(b'3\n')  # All Relays ON
                print("All Relays ON")
            elif fingers == 2:
                arduino.write(b'2\n')  # Relay 2 ON
                print("Relay 2 ON")
            elif fingers == 1:
                arduino.write(b'1\n')  # Relay 1 ON
                print("Relay 1 ON")
            else:
                arduino.write(b'0\n')  # All Relays OFF
                print("All Relays OFF")

    cv2.imshow("Hand Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()  # Close serial connection when finished
