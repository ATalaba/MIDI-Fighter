import threading, thread
import json
import sample_player
import sys
import termios

with open('mappings.json') as data_file:    
    	sample_mappings = json.load(data_file)

def get_ch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch

def button_listener(player):
	while True:
        c = get_ch()

        if c in sample_mappings:
        	sound_t = threading.Thread(target=player.play_sample, args=(sample_mappings[c]))
        	sound_t.daemon = True
			sound_t.start()
        elif c.lower() == 'q':
        	break
        else:
        	print "invalid command"

    os._exit(0)

if __name__ == '__main__':

	player = sample_player.SamplePlayer()
	t1 = threading.Thread(target=control_visualizer_settings, args=(player))
	t1.daemon = True
	t1.start()
