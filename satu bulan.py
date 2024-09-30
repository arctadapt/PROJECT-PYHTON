import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\n""Sudah adakah yang gantikanku", 0.10),
        ("Yang khawatirkanmu setiap waktu", 0.12),
        ("Yang cerita tentang apa pun sampai hal-hal tak perlu", 0.10),
        ("Kalau bisa, jangan buru-buru", 0.18),
        ("Kalau bisa, jangan ada dulu", 0.16),
    ]
    delays = [0.3, 5.5, 11.2, 16.0, 20.0]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()