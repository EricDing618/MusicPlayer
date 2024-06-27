from mp3player import *
from time import sleep

Musics = {
    "MainUI":"./music/mainui.mp3",
    "First":"./music/first.mp3",
    "Second":"./music/second.mp3",
    "Third":"./music/third.mp3",
    "Dead":"./music/dead.mp3",
    "Win":"./music/win.mp3",
    "End":"./music/money.mp3"
}
def test(seconds=15,name="MainUI",loop=True,musicdict:dict[str,str]=Musics):
    play = MusicPlayer(musicdict)
    play.go(name,loop)

    for i in range(seconds):
        print(f"{str(seconds-i)}...")
        sleep(1)

    play.stop()
    print('Stop!')

if __name__ == '__main__':
    test()