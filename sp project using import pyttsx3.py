import pyttsx3
engine=pyttsx3.init()
engine.setProperty('rate',100)


while True:
    answer=input("Enter what u want the robot want to say: ")
    engine.say(answer)
    engine.runAndWait()
    