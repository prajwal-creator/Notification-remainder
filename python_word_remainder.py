import time
from plyer import notification
import csv
import random

if __name__=="__main__":
    data=[]
    out=open("complete_dictionary.csv",'r')
    d = csv.reader(out)
    for row in d:
        data.append(row)
    while True:
        notification.notify(
            title = "Learn a new word",
            message = str(data[random.randint(0,len(data)-1)]),
            app_icon ="C:\\Users\\prajw\\OneDrive\\Desktop\\MY work\\Notification remainder\\dictionary.ico",
            timeout=6
        )
        time.sleep(10)
        out.close()
