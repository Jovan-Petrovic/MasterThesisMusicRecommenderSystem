from mutagen.mp3 import MP3
from pydub import AudioSegment
import os

'''
# find song bitrate
audio = MP3("000002.mp3")
bitrate = audio.info.bitrate / 1000
print(bitrate)

# files
src = "000002.mp3"
dst = "000002.wav"

# convert wav to mp3
audSeg = AudioSegment.from_mp3(src)
audSeg.export(dst, format="wav")
'''

root_mp3 = "C:/Users/proudsourceit/Desktop/MasterRad/Datasets/fma_small_by_genre"
for dirpath, dirnames, filenames in os.walk(root_mp3):
    if dirpath != root_mp3:
        root_wav = "C:/Users/proudsourceit/Desktop/MasterRad/Datasets/fma_small_by_genre_wav/" + dirpath.split("\\")[1]
        for filename in filenames:
            src = dirpath.replace("\\", "/") + "/" + filename
            dst = root_wav + "/" + filename.split(".")[0] + ".wav"
            try:
                audSeg = AudioSegment.from_mp3(src)
                audSeg.export(dst, format="wav")
            except:
                print("Error: " + src)
