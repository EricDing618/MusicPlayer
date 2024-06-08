from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"]="1" #禁用Pygame的输出

from pygame import mixer
from threading import Thread

class MusicPlayer:
    '''废弃项目（俄罗斯轮盘赌）的音乐播放器，可再利用。'''

    def __init__(self,MusicDict:dict):
        '''MusicDict：音频播放列表，Key是名称，Value是路径'''
        self.Musics=MusicDict

    def set_volume(self,n:int=100):
        self.volume = n / 100

        if self.volume > 1.0:
            self.volume=1.0
        elif self.volume < 0.0:
            self.volume=0.0

    def go(self,name:str="MainUI",loop=True):
        '''开始播放，name指字典中的某个key。'''
        self.mp3=name
        self.running=1
        self.playloop=loop

        self.playthread=Thread(target=self.__start)
        self.playthread.start()

    def stop(self):
        '''终止播放音频。'''
        self.running=0

    def thread_join(self,timeout=None):
        self.playthread.join(timeout)

    def __start(self):
        '''防止堵塞，使用多线程方式播放音频。'''
        mixer.init()
        mixer.music.load(self.Musics[self.mp3])
        mixer.music.play()
        while self.running:
            if mixer.music.get_busy() is False and self.playloop:
                mixer.music.play()
            else:
                break
                
        mixer.music.stop()
