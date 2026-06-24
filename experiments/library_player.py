import os
import sys

# Ensure project root is on sys.path so sibling packages (like `player`) import correctly
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from player.library import build_library
from player.audio_engine import AudioEngine

# Build library from absolute songs folder so running from any CWD works
songs_folder = os.path.join(ROOT, "songs")
library = build_library(songs_folder)

print("\n===== MUSIC LIBRARY =====\n")

for i, song in enumerate(library, start=1):
    print(f"{i}. {song['title']} ({song['duration']})")

choice = int(input("\nChoose song number: "))

selected_song = library[choice - 1]

print(f"\nNow Playing: {selected_song['title']}")

engine = AudioEngine()

# selected_song['path'] is produced by `player.library` and will be absolute when
# the library was built from an absolute `songs_folder`.
engine.play(selected_song["path"])