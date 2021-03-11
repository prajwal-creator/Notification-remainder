import time
from plyer import notification
import csv

if __name__=="__main__":
    while True:
        notification.notify(
            title = "Learn a new word",
            message = "petrified-mean scared",
            app_icon ="C:\\Users\\prajw\\OneDrive\\Desktop\\MY work\\Notification remainder\\dictionary.ico",
            timeout=6
        )
        time.sleep(60*60)
