from player.scanner import scan_songs
from player.metadata import extract_metadata

def build_library(folder_path):

    music_library = []

    songs = scan_songs(folder_path)

    for song in songs:

        metadata = extract_metadata(song)

        metadata["path"] = str(song)

        music_library.append(metadata)

    return music_library