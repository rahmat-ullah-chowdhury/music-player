import subprocess

song_path = "songs/Afreen Afreen Rath Fateh Ali Khan 128 Kbps.mp3"

args = [
    "ffmpeg",
    "-i",
    song_path
]

result = subprocess.run(
    args,
    capture_output=True,
    text=True
)

print(result.stderr)