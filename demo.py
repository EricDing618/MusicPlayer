from mp3player import *
from time import sleep

seconds = 15
Musics = {
    "MainUI":"./music/mainui.mp3",
    "First":"./music/first.mp3",
    "Second":"./music/second.mp3",
    "Third":"./music/third.mp3",
    "Dead":"./music/dead.mp3",
    "Win":"./music/win.mp3",
    "End":"./music/money.mp3"
}

play = MusicPlayer()
play.go()
play.GiveAMusicDict(Musics)

for i in range(seconds):
    print(f"{str(seconds-i)}...")
    sleep(1)

play.stop()
print('Stop!')