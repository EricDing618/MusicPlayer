from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"]="1" #禁用Pygame的输出

from pygame import mixer
from threading import Thread

class MusicPlayer:
    '''废弃项目（俄罗斯轮盘赌）的音乐播放器，可再利用。'''

    def __init__(self,MusicDict:dict):
        '''MusicDict：音频播放列表，Key是名称，Value是路径'''
        self.Musics=MusicDict
        self.volume=1.0

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
        if loop:
            self.playloop=-1
        else:
            self.playloop=0

        self.__start()

    def pause(yes=True):
        if yes:
            mixer.music.pause()
        else:
            mixer.music.unpause()
            
    def stop(self):
        '''终止播放音频。'''
        mixer.music.stop()

    def __start(self):
        mixer.init()
        mixer.music.load(self.Musics[self.mp3])
        mixer.music.play(self.playloop)
        mixer.music.set_volume(self.volume)

        
