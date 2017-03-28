import threading, thread
import json
import sample_player
import sys
import termios
import tty
import os
import wave

with open('mappings.json') as data_file:    
        sample_names = json.load(data_file)
        sample_mappings = {}
        for k, v in sample_names.iteritems():
            sample_mappings[k] = ''
            samp = wave.open(v, 'rb')
            periodsize = samp.getframerate()
            data = samp.readframes(periodsize)

            while data:
                # Read data from stdin
                sample_mappings[k] += data
                data = samp.readframes(periodsize)

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

        if c in sample_mappings:
            file_name = sample_names[c]
            data = sample_mappings[c]
            sound_t = threading.Thread(target=sample_player.play_sample, args=(file_name, data))
            sound_t.daemon = True
            sound_t.start()
        elif c.lower() == 'q':
            break
        else:
            print "invalid command"

    os._exit(0)

if __name__ == '__main__':

    t1 = threading.Thread(target=button_listener)
    t1.daemon = True
    t1.start()

    while True:
        pass
