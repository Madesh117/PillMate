import time
from datetime import datetime

# ------------------- VARIABLES -------------------
set_hour = -1
set_minute = -1

alarm_started = False
setting_time = False
selecting_meds = False
schedule_saved = False
alert_triggered = False

medicine_selected = [False, False, False, False]
input_buffer = ""

# ------------------- RESET FUNCTION -------------------
def reset_alarm_system():
    global alarm_started, setting_time, selecting_meds
    global schedule_saved, alert_triggered, input_buffer
    global medicine_selected

    alarm_started = False
    setting_time = False
    selecting_meds = False
    schedule_saved = False
    alert_triggered = False
    input_buffer = ""

    medicine_selected = [False, False, False, False]

    print("\nSystem Reset!\n")


# ------------------- DISPLAY -------------------
def display_time():
    now = datetime.now()
    print(f"\rTime {now.strftime('%H:%M:%S')}", end=" | ")

    if not alarm_started:
        print("Press # to Start", end="")
    elif setting_time:
        print(f"Set Time: {input_buffer}", end="")
    elif selecting_meds:
        meds = [str(i+1) for i, val in enumerate(medicine_selected) if val]
        print(f"Meds Selected: {''.join(meds)}", end="")
    elif schedule_saved:
        print("Alarm Set (#=Reset)", end="")


# ------------------- KEYPAD SIMULATION -------------------
def process_key(key):
    global alarm_started, setting_time, selecting_meds
    global schedule_saved, input_buffer
    global set_hour, set_minute

    # RESET
    if key == '#' and schedule_saved:
        reset_alarm_system()
        return

    # Start setup
    if not alarm_started and key == '#':
        alarm_started = True
        setting_time = True
        input_buffer = ""
        print("\nEnter time (HHMM): ")
        return

    # TIME INPUT
    if setting_time:
        if key.isdigit() and len(input_buffer) < 4:
            input_buffer += key

        elif key == '#' and len(input_buffer) == 4:
            entered_hour = int(input_buffer[:2])
            entered_minute = int(input_buffer[2:])

            now = datetime.now()
            current_total = now.hour * 60 + now.minute
            entered_total = entered_hour * 60 + entered_minute

            if entered_total <= current_total:
                print("\nPast Time! Try again.")
                input_buffer = ""
                return

            set_hour = entered_hour
            set_minute = entered_minute
            setting_time = False
            selecting_meds = True
            print("\nSelect Medicines (A-D), # to confirm")

    # MEDICINE SELECTION
    elif selecting_meds:
        if key in ['A', 'B', 'C', 'D']:
            index = ord(key) - ord('A')
            medicine_selected[index] = not medicine_selected[index]

        elif key == '#':
            selecting_meds = False
            schedule_saved = True
            print("\nAlarm Set Successfully!")


# ------------------- ALARM -------------------
def play_alarm():
    print("\n⏰ Pill Time! Take medicines!")

    selected = [i+1 for i, val in enumerate(medicine_selected) if val]
    print(f"Medicines to take: {selected}")

    start = time.time()

    while time.time() - start < 60:
        print("🔔 BEEP 🔔")
        time.sleep(0.5)


# ------------------- MAIN LOOP -------------------
def main():
    global alert_triggered

    while True:
        display_time()

        # Non-blocking input simulation
        if schedule_saved:
            now = datetime.now()
            if (now.hour == set_hour and 
                now.minute == set_minute and 
                now.second == 0):
                play_alarm()
                reset_alarm_system()

        # User input (simulate keypad)
        if input("\nPress key: ").strip():
            key = input().strip().upper()
            process_key(key)


if __name__ == "__main__":
    main()