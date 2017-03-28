import alsaaudio 

class SamplePlayer:

    def __init__(self, device='default'):
        self.device = alsaaudio.PCM(device=device)

       
    def play_sample(self, f):    

        print('%d channels, %d sampling rate\n' % (f.getnchannels(),
                                                   f.getframerate()))
        # Set attributes
        self.device.setchannels(f.getnchannels())
        self.device.setrate(f.getframerate())

        # 8bit is unsigned in wav files
        if f.getsampwidth() == 1:
            self.device.setformat(alsaaudio.PCM_FORMAT_U8)
        # Otherwise we assume signed data, little endian
        elif f.getsampwidth() == 2:
            self.device.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        elif f.getsampwidth() == 3:
            self.device.setformat(alsaaudio.PCM_FORMAT_S24_LE)
        elif f.getsampwidth() == 4:
            self.device.setformat(alsaaudio.PCM_FORMAT_S32_LE)
        else:
            raise ValueError('Unsupported format')

        periodsize = f.getframerate() / 8

        self.device.setperiodsize(periodsize)
        
        data = f.readframes(periodsize)
        while data:
            # Read data from stdin
            self.device.write(data)
            data = f.readframes(periodsize)
