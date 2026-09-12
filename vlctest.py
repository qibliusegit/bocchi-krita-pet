import vlc as v
import random
from pathlib import Path

song_dir = Path(__file__).parent / 'songs'
song_files = list(song_dir.rglob('*.mp3'))
file = random.choice(song_files)
print(file)

