import wave
import os

uname = os.uname()
if uname[0] == 'Linux':
    audio_lib_name = 'pyaudio'
else: 
    audio_lib_name = 'pyaudio'
audio_lib = __import__(audio_lib_name)

is_linux = False

def read(periodsize, i, frames, samp_width):
    return frames[i*periodsize*samp_width:(i+1)*periodsize*samp_width]

def play_sample(f, frames, dev='default'): 
    if is_linux:
        device = audio_lib.PCM(device=dev)
    else:
        # create an audio object
        p = audio_lib.PyAudio()
    
    samp = wave.open(f, 'rb')

    if is_linux:
        # Set attributes
        device.setchannels(samp.getnchannels())
        device.setrate(samp.getframerate())

        # 8bit is unsigned in wav files
        if samp.getsampwidth() == 1:
            device.setformat(audio_lib.PCM_FORMAT_U8)
        # Otherwise we assume signed data, little endian
        elif samp.getsampwidth() == 2:
            device.setformat(audio_lib.PCM_FORMAT_S16_LE)
        elif samp.getsampwidth() == 3:
            device.setformat(audio_lib.PCM_FORMAT_S24_LE)
        elif samp.getsampwidth() == 4:
            device.setformat(audio_lib.PCM_FORMAT_S32_LE)
        else:
            raise ValueError('Unsupported format')

        periodsize = samp.getframerate() / 8

        device.setperiodsize(periodsize)
    else:
        # open stream based on the wave object which has been input.
        device = p.open(format =
                    p.get_format_from_width(samp.getsampwidth()),
                    channels = samp.getnchannels(),
                    rate = samp.getframerate(),
                    output = True)
        periodsize = 1024

    i = 0
    data = read(periodsize, i, frames, samp.getsampwidth())

    while data:
        # Read data from stdin
        device.write(data)
        i += 1
        data = read(periodsize, i, frames, samp.getsampwidth())

    device.close() 
    if not is_linux:   
        p.terminate()
