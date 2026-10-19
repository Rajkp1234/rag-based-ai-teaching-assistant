
import os
import subprocess

files = os.listdir(".")

os.makedirs("../audios", exist_ok=True)

for file in files:
    if file.lower().endswith(".mp4"):
        subprocess.run([
            "ffmpeg", "-i", file,
            f"../audios/{os.path.splitext(file)[0]}.mp3"
        ])
