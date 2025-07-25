import os

def play_sound():
    os.system("termux-media-player play alarm.mp3 || echo '🎵 شغّل الصوت يدويًا'")
