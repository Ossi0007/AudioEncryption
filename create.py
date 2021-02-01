

import wave, struct, math, random

sampleRate = 44100.0 # hertz
duration = 1.0 # seconds
frequency = 440.0 # hertz
obj = wave.open('encrypted_sample.wav','w')
#obj.setnchannels(2) # mono
obj.setparams((2,2,8000,268237,'NONE','not compressed'))
print(obj.getparams())
# for i in range(99999):
#    value = random.randint(-32767, 32767)
#    data = struct.pack('<h', value)
#    obj.writeframesraw( data )
# obj.close()