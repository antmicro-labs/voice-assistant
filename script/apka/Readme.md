It's an exhibitive application, on which we are going to show capabilities of are voice assistant platform.

In order to make app work correctly you have to:
1. Invoke apt-get install mpg123
2. Invoke pip install -r requirements.txt
3. Open this link: https://developers.google.com/gmail/api/quickstart/python
4. Click 'Enable the Gmail API'
5. Select 'Desktop app' and download client configuration file which have to be placed in the project main folder
6. In MailHandler.py change the 'userID' to your email address
7. Upload some mp3 files to music folder and update list in MusicHandler.py
8. Make your own account on https://openweathermap.org/
9. Get the API key and put it in the 'key' variable in WeatherHandler.py
10. Install geckodriver:
    wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz
    sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.23.0-linux64.tar.gz -O > /usr/bin/geckodriver'
    sudo chmod +x /usr/bin/geckodriver
    rm geckodriver-v0.23.0-linux64.tar.gz
11. Invoke python3 responder.py to start application

In input.py file you can find list with mock commands. You can write your own set of instructions and test it.

