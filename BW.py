import datetime
'''import pyttsx3 for speaking happy birthday
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()'''
today=datetime.datetime.now()
print("Happy Birthday ",input("Enter the name: "),"\nDate: ",today.day," : ",today.month," : ",today.year)
