import climage
import os

class UI():

    def __init__(self):
        # You'll have to change the PATH to where the images are. Images are 0-whatever number

    def changeScreen(self, count):
        print(climage.convert("PATH TO IMAGES CHANGE THIS", is_unicode=True, is_truecolor=False, is_256color=False, is_16color=True, is_8color=False, width=120, palette="default"))

       # This is very rough on the eyes
#    def animation(self):
#        count = 0
#        while(1):
#            os.system("cls")
#            print(climage.convert("PATH TO IMAGES CHANGE THIS", is_unicode=False, is_truecolor=True, is_256color=False, is_16color=False, is_8color=False, width=120, palette="default"))
#            count += 1
#            if(count >= 28):
#                break
