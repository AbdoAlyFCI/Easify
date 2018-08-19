import pywinauto
import SpVoice
from pywinauto.keyboard import SendKeys 


#Feature class describe all variable and method that needed for every Feature 
class Feature():
    def __init__(self, key, keywords, sound, activate, jobKey):
        self.key = key
        self.keywords = keywords
        self.sound = sound
        self.activate = activate
        self.jobKey = jobKey
    def __repr__(self):
        return self.key
    def sendKeyStrokes(self):
        SendKeys(self.jobKey)
#mute Feature
mute = Feature("mute", ["mute"], True, True, None)
#endShow Feature
endShow = Feature("end show", ['end','stop'], True, True, "{VK_ESCAPE}")
startShow = Feature("start show", ['start'],True,True,"{F5}")
#previousSlide Feature
previousSlide=Feature("previous slide",['previous'],True,True,"{PGUP}")
#nextSlide Feature
nextSlide=Feature("next slide",['next'],True,True,"{PGDN}")
#unmute Feature
unmute=Feature("unmute",["unmute"],True,True,None)
#List for all current features
featuresList = [mute,endShow,startShow,previousSlide,nextSlide,unmute]


muted = False

#Step 3
#Choose the right functionality

def scan(word):
    global muted
    if muted==False :
        #Step 5 Apply  
        for i,feature in enumerate(featuresList):            
            if word in feature.keywords:
                if i==0:
                    muted=True
                    break
                else:
                    if feature.activate ==True:
                        feature.sendKeyStrokes()                    
                    break
                
    else:
        if word == "unmute":
            muted=False



            








            
                
