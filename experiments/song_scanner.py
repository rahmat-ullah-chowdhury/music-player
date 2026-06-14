from pathlib import Path


songs_folder = Path("songs")

for song in songs_folder.glob("*.mp3"):
    print(song.name)