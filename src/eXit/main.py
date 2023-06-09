import UI
import os

class main():

    def __init__(self):

        self.UI = UI.UI()

        self.story = ["You're trapped in a dungeon with your friend.\nYou see a barrel. What do you do?",
            "The barrel rolls aside and you find a secret tunnel. What do you do?",
            "You start to escape but your friend is too weak to\ngo with you. They hand you a note.\nWhat do you do?",
            "It is too dark to read the note.\nWhat do you do?",
            "You crawl through the tunnel and the tunnel leads\nto a beach. What do you do?",
            "In the water you see a boat.\nWhat do you do?",
            "Congratulations, you're heading to a new world!\nDo you want to play again?",
            "You're trapped in a dungeon with your friend... Is it\nthe same dungeon? You see a barrel. What do you do?",
            "Your friend hands you a note.\nWhat do you do?",
            "The note says, \"Don't leave me here.\"\nDo you leave your friend or stay?"]

        self.answers = ["move the barrel",
            "enter the tunnel",
            "read the note",
            "leave",
            "look",
            "get on the boat",
            "yes",
            "sit down next to my friend",
            "light a match",
            "stay"]

        self.inncorrectCount = 0

        self.inncorrect = ["You can't do that here.",
            "You can't do that now",
            "You could do that before",
            "You could do that later",
            "But it is now",
            "And it will always be now",
            "What is it, really?"]

        self.count = 0

    def anyKey(self):
        input("Press any key to start")
        self.clearConsole()

    def clearConsole(self):
        #too slow
        #command = 'clear'
        #if os.name in ('nt', 'dos'):  # If Machine is running on Windows (nt) or DOS.
        #    command = 'cls'
        #os.system(command)
        print('\033c', end='')

    def helloFriend(self):
        self.UI.changeScreen(str(self.count))
        self.anyKey()
        self.count += 1
        for s, a in zip(self.story, self.answers):
            self.UI.changeScreen(str(self.count))
            while True:
                print(s)
                answer = input("> ")
                if answer.lower() == a.lower():
                    self.count += 1
                    self.clearConsole()
                    break
                else:
                    self.clearConsole()
                    self.UI.changeScreen(str(self.count))
                    print(self.inncorrect[self.inncorrectCount])
                    self.inncorrectCount += 1
                    if self.inncorrectCount == 7:
                        self.inncorrectCount = 0

if __name__ == "__main__":
    bonsoirElliot = main()
    bonsoirElliot.helloFriend()

