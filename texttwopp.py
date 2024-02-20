import os
from gtts import gTTS
myText=input("write some bs: ")
language="en"
myObj=gTTS(text=myText, lang=language, slow=False)
myObj.save("shit.mp3")
os.system("mpg123 shit.mp3")
