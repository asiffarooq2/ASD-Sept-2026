# import time
# logfile = "activity_log.txt"
# def log_event(text):
#     with open(logfile, "a", encoding="utf-8") as f:
#         f.write(f"{time.ctime()} - {text}\n")
# log_event("Program is working")
# print("End of Program")

import time
import pyperclip
# import pyautogui
import os
import threading
import mss
logfile = "activity_log.txt"
screenshot_folder = "screenshots"
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

def log_event(text):
    with open(logfile, "a", encoding="utf-8") as f:
        f.write(f"{time.ctime()} - {text}\n")

def check_clipboard():
    data = pyperclip.paste()
    log_event(f"Clipboard: {data}")

# def save_screenshot():
#     filename = f"{screenshot_folder}/screenshot_{int(time.time())}.png"
#     pyautogui.screenshot(filename)
#     log_event(f"Screenshot: {filename}")

# def save_screenshot():
#     try:
#         filename = f"{screenshot_folder}/screenshot_{int(time.time())}.png"
#         pyautogui.screenshot(filename)
#         log_event(f"Screenshot: {filename}")
#     except Exception as e:
#         log_event(f"Screenshot Error: {e}")
def save_screenshot():
    try:
        with mss.MSS() as sct:
            filename = f"{screenshot_folder}/screenshot_{int(time.time())}.png"
            sct.shot(output=filename)
            log_event(f"Screenshot: {filename}")
    except Exception as e:
        log_event(f"Screenshot Error: {e}")

def monitor():
    for i in range(10):
        check_clipboard()
        save_screenshot()
        time.sleep(2)
print("Program Started.....")
log_event("Monitoring started")
monitor_thread = threading.Thread(target=monitor)
monitor_thread.start()
monitor_thread.join()
log_event("Monitoring finished")
print("Task Finished....")