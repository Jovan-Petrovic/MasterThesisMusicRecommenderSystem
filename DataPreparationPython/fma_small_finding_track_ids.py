import pandas as pd

indexes = []
#path to indexes file where all fma_small dataset track ids are stored
f = open(r"C:\Users\proudsourceit\IdeaProjects\jovan-master-side-work\indexes.txt", "r")
for x in f:
    indexes.append(x.replace('\n', '', 1))

print(indexes)

# path to fma dataset metadeta csv file
tracks = pd.read_csv("data/fma_metadata/tracks.csv")
df = pd.DataFrame(tracks)
# print(df)

df = df[['Unnamed: 0', 'track.7']]
df = df.rename(columns={'Unnamed: 0': 'track_id', 'track.7': 'genre'})
df = df.iloc[2:, :]
print(df)

removed = 0
for x in range(106574):
    if str(df.iloc[x - removed, 0]) not in indexes:
        df = df.drop(x+2)
        removed += 1
    else:
        print(df.iloc[x - removed, 0])


print(df)
df.to_csv("data/fma_small_tracks.csv")
print('END')