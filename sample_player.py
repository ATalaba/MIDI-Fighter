import wave
import os
import vlc

def play_sample(f): 
    p = vlc.MediaPlayer(f)
    p.play()

    #print p.audio_get_delay()