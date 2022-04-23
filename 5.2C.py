# Blue is on GPIO18 (port 12)
# Red is on GPIO14 (port 8)
# Green is on GPIO25 (port 22)

from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

#hardware
ledRed = LED(14)
ledBlue = LED(18)
ledGreen = LED(25)

# GUI Definitions
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

def reset():
    ledRed.off()
    ledBlue.off()
    ledGreen.off()
    ledRedButton["text"] = "Turn RED on"
    ledGreenButton["text"] = "Turn Green on"
    ledBlueButton["text"] = "Turn Blue on"
#Event Functions
def ledToggle(color):
    reset()
    if color == "Red":
        ledRed.on()
        ledRedButton["text"] = "Turn RED LED Off"
    elif color == "Green":
        ledGreen.on()
        ledGreenButton["text"] = "Turn Green LED Off"
    elif color == "Blue":
        ledBlue.on()
        ledBlueButton["text"] = "Turn Blue LED Off"

def close():
    RPi.GPIO.cleanup()
    win.destroy()

#Widgets
ledRedButton = Button(win, text = 'Turn Red LED On', font = myFont, command = lambda:ledToggle("Red"), bg = 'bisque2', height = 1, width = 24)
ledRedButton.grid(row=0, column =1)

ledBlueButton = Button(win, text = 'Turn Blue LED On', font = myFont, command = lambda:ledToggle("Blue"), bg = 'bisque2', height = 1, width = 24)
ledBlueButton.grid(row=1, column =1)

ledGreenButton = Button(win, text = 'Turn Green LED On', font = myFont, command = lambda:ledToggle("Green"), bg = 'bisque2', height = 1, width = 24)
ledGreenButton.grid(row=2, column =1)

exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'red', height = 1, width = 6)
exitButton.grid(row=3, column =1)

win.protocol("WM DELETE WINDOW", close)

win.mainloop()