import json
import pandas as pd

song_df = pd.read_excel('./music_list_7.xlsx')
song_df = song_df.where(pd.notnull(song_df), None)
song_list = []

for index, row in song_df.iterrows():
    # print(index, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
    song_data = {"index": index, "song_name": row[0], "artist": row[1], "language": row[2], "remarks": row[3], "initial": row[4], "sticky_top": row[5], "paid": row[6], "BVID": row[7]}
    if row[5] == 1:
        song_list.insert(0,song_data)
    else:
        song_list.append(song_data)
    

with open("./public/music_list_7.json", 'w') as file:
    file.write(json.dumps(song_list))
