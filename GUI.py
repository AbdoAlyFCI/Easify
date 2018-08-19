import _thread
from threading import Thread
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import time
from FeaturesClass import featuresList

from main import mymain
appliedFeatures = [['unmute']]
#Step 6 Starting the Process again
class MainThread(Thread):
    def __init__(self, function):
        self.running = False
        self.function = function
        super(MainThread, self).__init__()

    def start(self):
        self.running = True
        super(MainThread, self).start()

    def run(self):
        while self.running:
            self.function()

    def stop(self):
        self.running = False

root = Tk()
root.title("Easify")

content = ttk.Frame(root, width = 100, height = 300)
image = ImageTk.PhotoImage(Image.open("owl.png"))  # PIL solution
canv = Canvas(content, width=113, height=70)


feature1 = IntVar()
check1 = ttk.Checkbutton(content, text='Next slide', 
	    variable=feature1,onvalue=0,offvalue=1)

feature2 = IntVar()
check2 = ttk.Checkbutton(content, text='Previous Slide', 
	    variable=feature2,onvalue=0,offvalue=1)

feature3 = IntVar()
check3 = ttk.Checkbutton(content, text='start show', 
	    variable=feature3,onvalue=0,offvalue=1)

feature4 = IntVar()
check4 = ttk.Checkbutton(content, text='End show',                         
	    variable=feature4,onvalue=0,offvalue=1)

feature5 = IntVar()
check5 = ttk.Checkbutton(content, text='Mute/Unmute', 
	    variable=feature5,onvalue=0,offvalue=1)


featureList=[feature5,feature4,feature3,feature2,feature1]
def addFeatures():
    global appliedFeatures
   
    for i,feature in enumerate(featureList) :
        if feature.get() ==1:
            featuresList[i].activate=False
            print(featuresList[i].activate)
        else:
            featuresList[i].activate=True
            print(featuresList[i].activate)
    

ttk.Button(content, text="Refresh", command=addFeatures).grid(column=3, row=10)
content.grid(column=0, row=0)
canv.grid(row=0, column=2)
check1.grid(row = 5, column = 0)
check2.grid(row = 5, column = 3)
check3.grid(row = 7, column = 0)
check4.grid(row = 7, column = 3)
check5.grid(row = 8, column = 2)
canv.create_image(0, 0, anchor=NW, image=image)




threaded = MainThread(mymain)
try:
    threaded.start()
except (KeyboardInterrupt, SystemExit):
    cleanup_stop_thread();
    sys.exit()

root.mainloop()
threaded.stop()

print(appliedFeatures)
