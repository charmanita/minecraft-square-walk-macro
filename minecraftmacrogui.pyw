# Charmanita - Minecraft Macro with GUI
# 10/05/2025
# Basic Macro for Minecraft using Python, Pynput, and Tkinter
import time
import threading
from pynput import keyboard
import tkinter as tk
from tkinter import messagebox
import webbrowser
import webbrowser

TOGGLE_KEY = keyboard.KeyCode(char='b')
MOVEMENT_SEQUENCE = ['w', 'a', 's', 'd']

# Global state to control loop
is_running = False
keyboard_controller = keyboard.Controller()
movement_thread = None
time_per_side = 3.0  # Default time per side

def perform_square_movement():
    global is_running, time_per_side
    while is_running:
        for key in MOVEMENT_SEQUENCE:
            if not is_running:
                break

            print(f"Pressing {key.upper()} for {time_per_side} seconds...")

            keyboard_controller.press(key)
            time.sleep(time_per_side)
            keyboard_controller.release(key)
            time.sleep(0.1)  # Short pause between movements

    print("Macro stopped.")

def start_macro():
    global is_running, movement_thread
    if not is_running:
        is_running = True
        movement_thread = threading.Thread(target=perform_square_movement)
        movement_thread.daemon = True
        movement_thread.start()
        status_label.config(text="Status: Running", fg="green")
    else:
        messagebox.showinfo("Info", "Macro is already running.")

def stop_macro():
    global is_running
    if is_running:
        is_running = False
        status_label.config(text="Status: Stopped", fg="red")
    else:
        messagebox.showinfo("Info", "Macro is not running.")

def update_time_per_side():
    global time_per_side
    try:
        new_time = float(time_entry.get())
        if new_time > 0:
            time_per_side = new_time
            messagebox.showinfo("Info", f"Time per side updated to {time_per_side} seconds.")
        else:
            messagebox.showerror("Error", "Time must be a positive number.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

# GUI setup
def create_gui():
    global status_label, time_entry

    
    root = tk.Tk()
    root.iconbitmap("D:\Hrobe\Downloads\CodingProjects\Python\minecraftmacroicon.ico")
    root.title("Minecraft Macro")

    tk.Label(root, text="Minecraft Square Macro", font=("Arial", 16)).pack(pady=10)

    start_button = tk.Button(root, text="Start Macro", font=("Arial", 12), command=start_macro, bg="green", fg="white")
    start_button.pack(pady=5)

    stop_button = tk.Button(root, text="Stop Macro", font=("Arial", 12), command=stop_macro, bg="red", fg="white")
    stop_button.pack(pady=5)

    status_label = tk.Label(root, text="Status: Stopped", font=("Arial", 12), fg="red")
    status_label.pack(pady=10)

    tk.Label(root, text="Time per side (seconds):", font=("Arial", 10)).pack(pady=5)
    time_entry = tk.Entry(root, font=("Arial", 12))
    time_entry.pack(pady=5)
    time_entry.insert(0, str(time_per_side))  # Set default value

    update_button = tk.Button(root, text="Update Time", font=("Arial", 12), command=update_time_per_side, bg="blue", fg="white")
    update_button.pack(pady=5)

    tk.Label(root, text="You must have Minecraft focused for this to work.", font=("Arial", 10)).pack(pady=5)
    def open_github():
        webbrowser.open("https://github.com/charmanita/")

    def Discord():
        webbrowser.open("https://discord.com/users/485957450009149451")

    links_frame = tk.Frame(root)
    links_frame.pack(pady=10)

    github_button = tk.Button(links_frame, text="GitHub", font=("Arial", 10), command=open_github, fg="blue", cursor="hand2")
    github_button.pack(side="left", padx=5)

    discord_button = tk.Button(links_frame, text="DM me on Discord if bugs are found.", font=("Arial", 10), command=Discord, fg="blue", cursor="hand2")
    discord_button.pack(side="left", padx=5)
    root.mainloop()
create_gui()