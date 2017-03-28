import alsaaudio 
import wave

class SamplePlayer:

    def __init__(self, device='default'):
        self.device = alsaaudio.PCM(device=device)

       
    def play_sample(self, f):    
        samp = wave.open(f, 'rb')
        
        # Set attributes
        self.device.setchannels(samp.getnchannels())
        self.device.setrate(samp.getframerate())

        # 8bit is unsigned in wav files
        if samp.getsampwidth() == 1:
            self.device.setformat(alsaaudio.PCM_FORMAT_U8)
        # Otherwise we assume signed data, little endian
        elif samp.getsampwidth() == 2:
            self.device.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        elif samp.getsampwidth() == 3:
            self.device.setformat(alsaaudio.PCM_FORMAT_S24_LE)
        elif samp.getsampwidth() == 4:
            self.device.setformat(alsaaudio.PCM_FORMAT_S32_LE)
        else:
            raise ValueError('Unsupported format')

        periodsize = samp.getframerate() / 8

        self.device.setperiodsize(periodsize)
        
        data = samp.readframes(periodsize)
        while data:
            # Read data from stdin
            self.device.write(data)
            data = samp.readframes(periodsize)
