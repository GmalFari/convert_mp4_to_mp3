from moviepy.editor import *
mp4_file = "Video.mp4"
mp3_file = "audio.mp3"
videoclip = VideoFileClip(mp4_file)
audioClip = videoclip.audio
audioClip.write_audiofile(audioClip)
audioClip.close()
videoclip.close()
