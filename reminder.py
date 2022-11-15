# imports
from win10toast import ToastNotifier
import time # for timer

toaster = ToastNotifier()

title = input("\nTitle of Remainder: ")
msg = input("Message: ")
minutes = float(input("How many Minutes: "))

seconds = minutes * 60

print("\nRemainder Set Successfully!\n")
time.sleep(seconds)
toaster.show_toast(Toasttitle, msg, duration=10, threaded=True)

while toaster.notification_active:
    time.sleep(0.1)