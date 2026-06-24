import os
import subprocess

def extract_metadata(song_path):

    title = None
    artist = None
    album = None
    duration = None

    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format_tags=title:format_tags=artist:format_tags=album:format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(song_path),
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        for line in result.stdout.splitlines():
            line = line.strip()
            if not line:
                continue
            if line.startswith("TAG:title="):
                title = line.split("=", 1)[1]
            elif line.startswith("TAG:artist="):
                artist = line.split("=", 1)[1]
            elif line.startswith("TAG:album="):
                album = line.split("=", 1)[1]
            elif line.startswith("duration="):
                duration = line.split("=", 1)[1]

    if not title:
        title = os.path.splitext(os.path.basename(song_path))[0]
    if not artist:
        artist = "Unknown"
    if not album:
        album = "Unknown"
    if not duration:
        duration = "Unknown"

    return {
        "title": title,
        "artist": artist,
        "album": album,
        "duration": duration,
    }