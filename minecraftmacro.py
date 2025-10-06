# Charmanita - Minecraft Macro
# 10/05/2025
# Basic Macro for Minecraft using Python and Pynput
import time
import threading
from pynput import keyboard
TOGGLE_KEY = keyboard.KeyCode(char='b')
TIME_PER_SIDE = 3.0
MOVEMENT_SEQUENCE = ['w', 'a', 's', 'd']
# -------------
# Global state to control loop
is_running = False
# Controller for simulating key presses
keyboard_controller = keyboard.Controller()
movement_thread = None

def perform_square_movement():
    while is_running:  # Keep looping while is_running is True
        for key in MOVEMENT_SEQUENCE:
            if not is_running: 
                break

            print(f"Pressing {key.upper()} for {TIME_PER_SIDE} seconds...")

            keyboard_controller.press(key)
            time.sleep(TIME_PER_SIDE)
            keyboard_controller.release(key)
            time.sleep(0.1)  # Short pause between movements

    print("Macro stopped.")

def on_press(key):
    global is_running, movement_thread

    try: 
        if key == TOGGLE_KEY:
            if is_running:
                is_running = False
            else:
                is_running = True

                movement_thread = threading.Thread(target=perform_square_movement)
                movement_thread.daemon = True
                movement_thread.start()
    except Exception as e:
        print(f"An error occurred. {e}")


def start_listener(): 
    print("--- Minecraft Square Macro Initialized ---")


    key_display = str(TOGGLE_KEY.char).upper() if hasattr(TOGGLE_KEY, 'char') and TOGGLE_KEY.char else TOGGLE_KEY.name.upper()

    print(f"Ready. Press '{key_display}' to start/stop the macro.")
    print(f"You must have Minecraft focused for this to work.")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_listener()
