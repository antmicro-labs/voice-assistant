from pygame import mixer

songs = ['music/mozart_40_g.oga', 'music/bethoven_5th.ogg']

class MusicHandler:
    def __init__(self):
        self.currentlyPlaying = 0
        self.currentVolume = 0.1
        mixer.init()
        mixer.music.set_volume(self.currentVolume)

    def startMusic(self):
        mixer.music.load(songs[self.currentlyPlaying])
        mixer.music.play()

    def stopMusic(self):
        mixer.music.stop()
        return None

    def volumeUp(self):
        self.currentVolume += 0.8
        if self.currentVolume > 1.0:
            self.currentVolume = 1.0
        mixer.music.set_volume(self.currentVolume)

    def volumeDown(self):
        self.currentVolume -= 0.8
        if self.currentVolume < 0.0:
            self.currentVolume = 0.0
        mixer.music.set_volume(self.currentVolume)

    def nextSong(self, num):
        self.currentlyPlaying += num
        numOfSOngs = self.currentlyPlaying = len(songs) -1
        if self.currentlyPlaying < 0:
            self.currentlyPlaying = numOfSOngs
        elif self.currentlyPlaying > numOfSOngs:
            self.currentlyPlaying = 0
        mixer.music.load(songs[self.currentlyPlaying])
        mixer.music.play()

    def unpauseSong(self):
        mixer.music.unpause()

    def pauseSong(self):
        mixer.music.pause()