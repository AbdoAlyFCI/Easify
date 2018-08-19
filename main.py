#© Copyright 2018, Mark Mc Mahon and Contributors for pywinauto & pywinauto.keyboard library
#this is a part from the SpeechRecognition module in Python all copyright reseved for the owner

#Easify work Divide into 5 main steps
#1-voice input --->main.py 
#2-send to Google voice recognize API --->SpVoice.py
#3-Outcome String form Google API  --->main.py to FeaturesClass.py
#4-Choose the right functionality  --->FeaturesClass.py
#5-Apply it --->with FeatureClass.py on the current Application (ex:Microsoft Power Point)
#6-Start again   --->threat in GUI.py
#note it is just a prototype for test use with the ability to enhance it in the future




from FeaturesClass import scan
from SpVoice import check_audio

def mymain():

    #Start of the main Program
     
    print("1")
    #Step 1 voice input
    
    OutComeString=check_audio()
    if(OutComeString =="no any rec"):
        print()          
    else :
        #Step 3 Outcome String form Google API
        print(OutComeString)
        scan(OutComeString)
