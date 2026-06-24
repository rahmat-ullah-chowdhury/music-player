import subprocess


class AudioEngine:

    def play(self, song_path):

        subprocess.Popen(
            [
                "ffplay",
                "-nodisp",
                "-autoexit",
                song_path
            ]
        )

    def stop(self):
        pass