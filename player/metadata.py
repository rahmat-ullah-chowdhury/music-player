import subprocess
import re

def extract_metadata(song_path):

    result = subprocess.run(
        ["ffmpeg", "-i", str(song_path)],
        capture_output=True,
        text=True
    )

    output = result.stderr

    title = re.search(r"title\s*:\s*(.+)", output)
    artist = re.search(r"artist\s*:\s*(.+)", output)
    album = re.search(r"album\s*:\s*(.+)", output)
    duration = re.search(r"Duration:\s*([0-9:.]+)", output)

    return {
        "title": title.group(1) if title else "Unknown",
        "artist": artist.group(1) if artist else "Unknown",
        "album": album.group(1) if album else "Unknown",
        "duration": duration.group(1) if duration else "Unknown"
    }