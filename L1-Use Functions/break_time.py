import webbrowser
import time

#This program opens up a web page after waiting 10 seconds, then repeats two more times
break_count = 0
break_total = 3
print("This program started on " + time.ctime())
while (break_count < break_total):
    time.sleep(5)
    webbrowser.open("https://classroom.udacity.com/courses/ud036/lessons/993460168/concepts/9977893120923")
    break_count = break_count + 1

