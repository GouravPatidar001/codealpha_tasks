import time
import psutil
import pyautogui
from plyer import notification
import tkinter as tk
from threading import Thread

def check_running_apps():
    """Check if Instagram or YouTube is running."""
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] in ['chrome.exe', 'msedge.exe', 'firefox.exe']:  # Browsers where Instagram/Youtube might be open
            return True
    return False

def display_notification():
    """Display notification to quit the app."""
    notification.notify(
        title="Time to Take a Break",
        message="You've been watching Reels/Shorts for 5 minutes. Consider taking a break.",
        timeout=10
    )

def quit_apps():
    """Quit Instagram or YouTube."""
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] in ['chrome.exe', 'msedge.exe', 'firefox.exe']:
            proc.terminate()

def create_gui():
    """Create a simple GUI with two buttons."""
    root = tk.Tk()
    root.title("Control Instagram and YouTube Usage")
    root.geometry("300x100")

    def quit_and_close():
        quit_apps()
        root.destroy()

    def close():
        root.destroy()

    quit_button = tk.Button(root, text="Quit Instagram/YouTube", command=quit_and_close)
    quit_button.pack(pady=10)

    cancel_button = tk.Button(root, text="Cancel Software", command=close)
    cancel_button.pack(pady=10)

    root.mainloop()

def start_monitoring():
    """Start monitoring Instagram and YouTube usage."""
    while True:
        if check_running_apps():
            display_notification()
            create_gui()
        time.sleep(300)  # Wait for 5 minutes before checking again

if __name__ == "__main__":
    monitoring_thread = Thread(target=start_monitoring)
    monitoring_thread.start()
