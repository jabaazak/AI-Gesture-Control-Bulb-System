# AI-Gesture-Control-Bulb-System

🤖 AI-based Hand Gesture Control System

This project is an AI-powered hand gesture control system that allows you to control series of bulb using just your hand movements. It combines Python (for gesture recognition) with Arduino UNO (for hardware control) and a 2-channel relay module to switch devices on/off.

📌 Features

✋ Hand gesture recognition using MediaPipe

🔗 Serial communication between Python and Arduino using pyserial

⚡ Control home appliances (lights, fans, etc.) via relay module

🌐 Integration with requests for HTTP-based control (expandable to smart assistants like Alexa)

💡 Real-time, touchless control system for smart homes

🛠️ Components Used

Arduino UNO

2-Channel Relay Module

Laptop/PC Camera (for hand detection)

Jumper Wires & Breadboard

Home Appliances (for demonstration)

💻 Software & Libraries

Python: mediapipe, pyserial, requests

Arduino IDE: C/C++ for Arduino UNO programming

⚙️ How It Works

The camera captures your hand gestures.

Python processes the frame using MediaPipe to detect hand landmarks.

Detected gestures are sent via serial communication (pyserial) to the Arduino UNO.

Arduino UNO controls the relay module, which switches appliances ON/OFF.
