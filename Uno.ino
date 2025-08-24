#define RELAY1 7  // Connected to IN1
#define RELAY2 8  // Connected to IN2

void setup() {
    Serial.begin(9600);  // Start Serial Communication
    pinMode(RELAY1, OUTPUT);
    pinMode(RELAY2, OUTPUT);
    digitalWrite(RELAY1, HIGH);  // Start with relays OFF
    digitalWrite(RELAY2, HIGH);
}

void loop() {
    if (Serial.available()) {
        char command = Serial.read();  // Read data from Serial
        
        if (command == '3') {
            digitalWrite(RELAY1, LOW);  // Relay 1 ON
            digitalWrite(RELAY2, LOW);  // Relay 2 ON
        }
        else if (command == '2') {
            digitalWrite(RELAY1, HIGH); // Relay 1 OFF
            digitalWrite(RELAY2, LOW);  // Relay 2 ON
        }
        else if (command == '1') {
            digitalWrite(RELAY1, LOW);  // Relay 1 ON
            digitalWrite(RELAY2, HIGH); // Relay 2 OFF
        }
        else if (command == '0') {
            digitalWrite(RELAY1, HIGH); // Relay 1 OFF
            digitalWrite(RELAY2, HIGH); // Relay 2 OFF
        }
    }
}
