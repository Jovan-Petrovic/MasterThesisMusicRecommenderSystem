import os
import pandas as pd
import shutil

def removeZerosBeforeFirstNonZeroDigit(number):
    for i, v in enumerate(number):
        if v != '0':
            return number[i:]

df = pd.read_csv("fma_small_tracks.csv")
song_id_series = df['track_id']
genre_series = df['genre']

rootdir = 'C:/Users/proudsourceit/Desktop/MasterRad/Datasets/fma_small'
for dirpath, dirnames, filenames in os.walk(rootdir):
    for dir in dirnames:
        for dirpath1, dirnames1, filenames1 in os.walk(rootdir + '/' + dir):
            for filename1 in filenames1:
                song_id = removeZerosBeforeFirstNonZeroDigit(filename1).replace(".mp3", "")
                genre = genre_series[song_id_series[song_id_series == int(song_id)].index[0]]
                original = rootdir + "/" + dir + "/" + filename1
                target = rootdir.replace("fma_small", "fma_small_by_genre") + "/" + genre + "/" + filename1
                shutil.copyfile(original, target)
