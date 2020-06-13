from subprocess import Popen, PIPE
from Menu import Menu
from MusicHandler import MusicHandler
from MailHandler import MailHandler

menu = Menu()
mail = MailHandler()
music = MusicHandler()

cmd = "python3 input.py"
process = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True, bufsize=1)

choosenOption = None

while True:
    out = process.stdout.readline()
    out = out.decode("utf-8").strip()
    if choosenOption is None:
        if out == 'go':
            menu.readCurrOption()

        elif out == 'right':
            menu.readNextOption(1)

        elif out == 'left':
            menu.readNextOption(-1)

        elif out == 'on':
            choosenOption = menu.chooseCurrOption()

    elif choosenOption == 'Odtwarzacz muzyki':
        if out == 'go':
            music.startMusic()

        elif out == 'stop':
            choosenOption = music.stopMusic()

        elif out == 'up':
            music.volumeUp()

        elif out == 'down':
            music.volumeDown()

        elif out == 'right':
            music.nextSong(1)

        elif out == 'left':
            music.nextSong(-1)

        elif out == 'on':
            music.unpauseSong()

        elif out == 'off':
            music.pauseSong()

    elif choosenOption == 'Zobacz pogode':
        pass

    elif choosenOption == 'Sprawdź poczte':
        if out == 'go':
            mail.getMails()

        elif out == 'yes':
            mail.readMails()

        elif out == 'no':
            choosenOption = mail.stopReading()
            
