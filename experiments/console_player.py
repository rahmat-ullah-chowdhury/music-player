import os
import sys

# Fix imports
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from player.library import build_library
from player.audio_engine import AudioEngine

# Build music library
songs_folder = os.path.join(ROOT, "songs")
library = build_library(songs_folder)

# Audio player
engine = AudioEngine()

# Keep track of currently playing song
current_song_index = None

while True:

    print("\n===== MUSIC PLAYER =====")
    print("1. Show Songs")
    print("2. Play Song")
    print("3. Stop Song")
    print("4. Next Song")
    print("5. Previous Song")
    print("6. Exit")

    choice = input("Choice: ")

    # Show songs
    if choice == "1":

        print("\n===== SONG LIST =====")

        for i, song in enumerate(library, start=1):

            print(
                f"{i}. {song['title']} "
                f"({song['duration']})"
            )

    # Play selected song
    elif choice == "2":

        song_number = int(input("Song number: "))

        if 1 <= song_number <= len(library):

            current_song_index = song_number - 1

            selected_song = library[current_song_index]

            print(f"\nNow Playing: {selected_song['title']}")

            engine.play(selected_song["path"])

        else:

            print("Invalid song number.")

    # Stop song
    elif choice == "3":

        engine.stop()

        print("Song stopped.")

    # Next song
    elif choice == "4":

        if current_song_index is None:

            print("Play a song first.")

        else:

            current_song_index += 1

            if current_song_index >= len(library):
                current_song_index = 0

            selected_song = library[current_song_index]

            print(f"\nNow Playing: {selected_song['title']}")

            engine.play(selected_song["path"])

    # Previous song
    elif choice == "5":

        if current_song_index is None:

            print("Play a song first.")

        else:

            current_song_index -= 1

            if current_song_index < 0:
                current_song_index = len(library) - 1

            selected_song = library[current_song_index]

            print(f"\nNow Playing: {selected_song['title']}")

            engine.play(selected_song["path"])

    # Exit
    elif choice == "6":

        engine.stop()

        print("Goodbye!")
        break

    else:

        print("Invalid choice.")

        print("Invalid choice.")