from utils import textReader

class Menu:
    def __init__(self):
        self.currOptionNum = 0
        self.mainMenu = ['Music player', 'Current weather', 'Check emails', 'Find random recipe']

    def readCurrOption(self):
        currOption = self.mainMenu[self.currOptionNum]
        textReader(currOption)

    def readNextOption(self, num):
        self.currOptionNum += num
        self.currOptionNum %= len(self.mainMenu)
        self.readCurrOption()

    def chooseCurrOption(self):
        choosenOption = 'You have chosen ' + self.mainMenu[self.currOptionNum]
        textReader(choosenOption)
        return self.mainMenu[self.currOptionNum]
