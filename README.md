# MusicPlayer
使用Python做的轻量级音频播放器。

# 示例
- 见`demo.py`。

# 方法（示例）
- `play = MusicPlayer({"name1":"path1","name2":"path2",...})`：创建一个播放器并自定义音频列表。
- `play.go("name1")`：播放`key`为`name1`的`value`（音频路径）。
- `play.stop()`：终止播放音频。
