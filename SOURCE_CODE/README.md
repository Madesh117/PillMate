# 💊 Smart Pill Reminder System (ESP32)

## 🧠 What is this project?
This project is a simple **smart pill reminder system** built using an ESP32.  
The idea is to help people remember to take their medicines on time without relying on memory or manual tracking.

Instead of just giving a notification, this system actually:
- Alerts the user using sound and lights  
- Shows details on an LCD screen  
- Opens the medicine compartment using a servo motor  

So it’s not just a reminder — it’s a **mini automated medicine assistant**.

---

## ⚙️ How it works (in simple words)

1. When the system starts, it shows the current time on the LCD.
2. You press `#` to begin setting your alarm.
3. Enter the time in **HHMM format** (for example: 0930 for 9:30 AM).
4. Then choose which medicines you want:
   - `A`, `B`, `C`, `D` → different medicine slots
5. Once saved, the system waits.

👉 At the exact time:
- Buzzer starts beeping 🔔  
- LEDs glow 💡  
- Servo motors rotate ⚙️ (dispense medicine)  
- LCD shows **"Pill Time!"**

You can stop the alarm using `*` or reset using `#`.

---

## 🧰 Components used

- ESP32 (main controller)
- 16x2 LCD (I2C)
- 4 LEDs (for indication)
- Buzzer (for alert sound)
- 4 Servo motors (to release pills)
- 4x4 Keypad (for input)
- RTC module (DS1307)
- Resistors, wires, breadboard

---

## 🔌 Circuit design

The full circuit is designed using Wokwi simulator.

Import the provided JSON file into Wokwi to view the connections.

---

## 💻 Code

The main logic is written in Arduino (ESP32).  
It handles:
- Time synchronization
- Keypad input
- Display updates
- Alarm triggering
- Servo and buzzer control

---

## ▶️ How to run this project

### 🟢 Option 1: Simulation (easy)
1. Open Wokwi
2. Upload the code + JSON file
3. Start simulation
4. Use keypad on screen

### 🟢 Option 2: Real hardware
1. Connect all components properly
2. Upload code using Arduino IDE
3. Power the ESP32
4. Set your alarm and test

---

## ⚠️ Limitations

- Only supports 4 medicines  
- No mobile app or notifications  
- Needs manual setup  
- No battery backup  

---

## 🚀 Future Improvements

- Mobile app integration  
- Cloud notifications  
- Automatic schedule storage  
- Voice assistant support  
- Health tracking dashboard  


