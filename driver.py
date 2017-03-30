import threading
import json
import sample_player
import sys
import termios
import tty
import os
import wave


with open('mappings.json') as data_file:    
        sample_names = json.load(data_file)

def get_ch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch

def button_listener():
    while True:
        c = get_ch()

        if c in sample_names:
            file_name = sample_names[c]
            sound_t = threading.Thread(target=sample_player.play_sample, args=(file_name, ))
            sound_t.daemon = True
            sound_t.start()
        elif c.lower() == 'q':
            break
        else:
            print("invalid command")


    os._exit(0)

if __name__ == '__main__':

    t1 = threading.Thread(target=button_listener)
    t1.daemon = True
    t1.start()

    while True:
        pass
