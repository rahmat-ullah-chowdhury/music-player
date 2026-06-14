from pathlib import Path

from metadata_parser import extract_metadata


songs_folder = Path("songs")

music_library = []

for song in songs_folder.glob("*.mp3"):

    metadata = extract_metadata(song)

    music_library.append(metadata)

print("\n===== MUSIC LIBRARY =====\n")

for index, song in enumerate(music_library, start=1):

    print(f"Song #{index}")

    print("Title    :", song["title"])
    print("Artist   :", song["artist"])
    print("Album    :", song["album"])
    print("Duration :", song["duration"])

    print("-" * 40)