from pathlib import Path

def scan_songs(folder_path):
    return list(Path(folder_path).glob("*.mp3"))