import os
import sys
import time

# Ensure project root is on sys.path so sibling packages like `player` import correctly
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from player.audio_engine import AudioEngine

engine = AudioEngine()

print("Playing song...")

song = os.path.join(ROOT, "songs", "Afreen Afreen Rath Fateh Ali Khan 128 Kbps.mp3")
if not os.path.exists(song):
    raise FileNotFoundError(f"Song not found: {song}")

engine.play(song)

time.sleep(5)

print("Stopping song...")

engine.stop()