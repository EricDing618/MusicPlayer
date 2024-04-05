from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"]="1" #禁用Pygame的输出

from pygame import mixer
from threading import Thread

class MusicPlayer:
    '''废弃项目（俄罗斯轮盘赌）的音乐播放器，可再利用。'''

    def __init__(self):

        self.Musics={ #默认字典，格式：{名称:路径,...}
            "MainUI":"./music/主界面.mp3",
            "First":"./music/第一场.mp3",
            "Second":"./music/第二场.mp3",
            "Third":"./music/第三场.mp3",
            "Dead":"./music/被击败.mp3",
            "Win":"./music/击败对方.mp3",
            "End":"./music/结算美元.mp3"
        }

    def go(self,name:str="MainUI"):
        '''开始播放，name指字典中的某个key。'''
        self.mp3=name
        self.running=1
        Thread(target=self.__start).start()

    def GiveAMusicDict(self,musicdict: dict|None = None):
        '''替换默认播放字典。'''
        if musicdict is not None:
            self.Musics=musicdict

    def stop(self):
        '''终止播放音频。'''
        self.running=0

    def __start(self):
        '''防止堵塞，使用多线程方式播放音频。'''
        mixer.init()
        mixer.music.load(self.Musics[self.mp3])
        mixer.music.play()
        while self.running:
            if mixer.music.get_busy():
                pass
            else:
                mixer.music.play()
        mixer.music.stop()

def demo(): #示例
    seconds=15
    play=MusicPlayer()
    play.go()
    play.GiveAMusicDict()
    from time import sleep
    for i in range(seconds):
        print(f"{str(seconds-i)}...")
        sleep(1)
    play.stop()
    print('Stop!')

if __name__ == "__main__":
    demo()