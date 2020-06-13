from utils import textReader

class Menu:
    def __init__(self):
        self.currOptionNum = 0
        self.mainMenu = ['Odtwarzacz muzyki', 'Zobacz pogode', 'Sprawdź poczte']

    def readCurrOption(self):
        currOption = self.mainMenu[self.currOptionNum]
        textReader(currOption)

    def readNextOption(self, num):
        self.currOptionNum += num
	self.currOptionNum %= len(self.mainMenu)
        self.readCurrOption()

    def chooseCurrOption(self):
        choosenOption = 'Wybrano opcje, ' + self.mainMenu[self.currOptionNum]
        textReader(choosenOption)
        return self.mainMenu[self.currOptionNum]
