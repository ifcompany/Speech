# Telegar : @Thelinkif
from gtts import gTTS
from os import system
system("cls")
logp = '''
    \033[0;37m|\033[0;36m Text \033[0;37m|\033[0;32m ~~\033[0;33m> \033[0;37m| \033[0;36mSound \033[0;37m|

   \033[0;35m { \033[0;32mT\033[0;33m.\033[0;32mSound          \033[0;35m}
   \033[0;35m { \033[4;34mifcompany\033[4;33m.\033[4;34mir\033[0;35m     }
   \033[0;35m [\033[0;36m Programmer \033[0;33m: \033[0;101m007\033[0;35m ] \033[0;33mV \033[0;32m1.0.0 \033[0;33mWindows\033[0m
'''
print(logp)
etext = input("\033[0;37m[\033[0;32m$\033[0;37m]\033[0;36m Pls Enter Text \033[0;33m\> \033[0m")
users = input("\033[0;37m[\033[0;32m$\033[0;37m]\033[0;36m Pls Enter \033[0;31mUser \033[0;36mPC \033[0;37m(\033[0;32mc://Users/\033[0;31m?\033[0;32m/Desktop\033[0;37m) \033[0;33m\> \033[0m")
sound = gTTS(text=etext, lang='en')
sound.save("c://Users/"+ users + "/Desktop/" + etext.replace(" ","-") + ".mp3")
system("start c://Users/"+ users + "/Desktop/" + etext.replace(" ","-") + ".mp3")
print("\033[0;37m[\033[0;32m#\033[0;37m] \033[0;36mAn audio file named \033[0;33m: \033[0;32m" + etext.replace(" ","-") + ".mp3 \033[0;33m, \033[0;36m Was created in the Desktop\033[0m")