from pydub import AudioSegment
from pydub.playback import play


class Player:

    def __init__(self):
        self._running = True
        self.sound = AudioSegment.from_file("appatcher/music/keygenref.mp3",
                                            format="mp3")

    def terminate(self):
        # self.playback.stop()
        self._running = False

    def run(self):
        self._running = True

        while self._running:
            play(self.sound)
            # self.playback = _play_with_simpleaudio(self.sound)

    def isRunning(self):
        return self._running
