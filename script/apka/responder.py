from subprocess import Popen, PIPE
from Menu import Menu
from MusicHandler import MusicHandler
from MailHandler import MailHandler
from WeatherHandler import WeatherHandler
from URLHandler import URLHandler

menu = Menu()
# mail = MailHandler()
music = MusicHandler()
weather = WeatherHandler()
urlHandler = URLHandler()

cmd = "python3 input.py"
process = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True, bufsize=1)

choosenOption = None

while True:
    out = process.stdout.readline()
    out = out.decode("utf-8").strip()
    print("Incoming command: ", out)
    if choosenOption is None:
        if out == 'VA:CMD:GO':
            menu.readCurrOption()

        elif out == 'VA:CMD:RIGHT':
            menu.readNextOption(1)

        elif out == 'VA:CMD:LEFT':
            menu.readNextOption(-1)

        elif out == 'VA:CMD:ON':
            choosenOption = menu.chooseCurrOption()

    elif choosenOption == 'Music player':
        if out == 'VA:CMD:GO':
            music.startMusic()

        elif out == 'VA:CMD:STOP':
            choosenOption = music.stopMusic()

        elif out == 'VA:CMD:UP':
            music.volumeUp()

        elif out == 'VA:CMD:DOWN':
            music.volumeDown()

        elif out == 'VA:CMD:RIGHT':
            music.nextSong(1)

        elif out == 'VA:CMD:LEFT':
            music.nextSong(-1)

        elif out == 'VA:CMD:ON':
            music.unpauseSong()

        elif out == 'VA:CMD:OFF':
            music.pauseSong()

    elif choosenOption == 'Current weather':
        if out == 'VA:CMD:GO':
            choosenOption = weather.getWeather()

    elif choosenOption == 'Find random recipe':
        if out == 'VA:CMD:GO':
            choosenOption = urlHandler.openURL()

    elif choosenOption == 'Check emails':
        if out == 'VA:CMD:GO':
            # mail.getMails()
            pass

        elif out == 'VA:CMD:YES':
            # mail.readMails()
            pass

        elif out == 'VA:CMD:NO':
            # choosenOption = mail.stopReading()
            pass
        