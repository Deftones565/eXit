import climage
import os

class UI():

    def __init__(self):
        self.location = os.getcwd()
        self.image = "\\images\\"
        self.screen = "0"
        self.png = ".png"
        self.animationPath = "animation\\"

    def changeScreen(self, count):
        print(climage.convert(self.location+self.image+count+self.png, is_unicode=True, is_truecolor=False, is_256color=False, is_16color=True, is_8color=False, width=120, palette="default"))

    # This is rough on the eyes
#    def animation(self):
#        count = 0
#        while(1):
#            os.system("cls")
#            print(climage.convert(self.location+self.animationPath+str(count)+self.png, is_unicode=False, is_truecolor=True, is_256color=False, is_16color=False, is_8color=False, width=120, palette="default"))
#            count += 1
#            if(count >= 28):
#                break
