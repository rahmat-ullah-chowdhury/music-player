import os
import sys

# Ensure project root is on sys.path so sibling packages (like `player`) import correctly
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
	sys.path.insert(0, ROOT)

from player.audio_engine import AudioEngine

engine = AudioEngine()

# Use an absolute path to the song so running the script from any CWD works
song = os.path.join(ROOT, "songs", "Afreen Afreen Rath Fateh Ali Khan 128 Kbps.mp3")
if not os.path.exists(song):
	raise FileNotFoundError(f"Song not found: {song}")

try:
	engine.play(song)
except FileNotFoundError as e:
	# subprocess raises FileNotFoundError when the executable (ffplay) is missing
	raise RuntimeError("ffplay (FFmpeg) not found. Install FFmpeg and add ffplay to PATH.") from e