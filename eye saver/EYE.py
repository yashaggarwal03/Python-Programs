import time
from plyer import notification

if __name__ == "__main__":
     while True:
         notification.notify(
             title = "Take a rest please",
             message = "You are using your PC from last 1 hour please give rest to your eyes",
             app_icon = r"C:\Users\admin\Desktop\codeing\PYTHON\eye saver\Images\eyes.ico",
             timeout=15
         )
         time.sleep(60*60)