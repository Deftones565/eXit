import climage
import os

class UI():

    def __init__(self):
        self.location = os.getcwd()
        self.image = "images"
        self.screen = "0"
        self.png = ".png"
        self.animationPath = "animation"

    def changeScreen(self, count):
        image_path = os.path.join(self.location, self.image, count+self.png)
        print(climage.convert(image_path, is_unicode=True, is_truecolor=False, is_256color=False, is_16color=True, is_8color=False, width=120, palette="default"))

    # This is rough on the eyes
#    def animation(self):
#        count = 0
#        while(1):
#            os.system("cls")
#            animation_path = os.path.join(self.location, self.animationPath, str(count) + self.png)
#            print(climage.convert(animation_path, is_unicode=False, is_truecolor=True, is_256color=False, is_16color=False, is_8color=False, width=120, palette="default"))
#            count += 1
#            if(count >= 28):
#                break

