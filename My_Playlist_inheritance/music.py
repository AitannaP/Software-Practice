import pandas as pd
from pathlib import Path


class Music:
    final_list_of_songs = []

    def __init__(self , title, artist):
        self.title = title
        self.artist = artist


class HipHop(Music):
    def __init__(self,title, artist):
       super().__init__(title, artist)

class Pop(Music):
    def __init__(self,title, artist):
        super().__init__(title, artist)

class OtherGenre(Music):
    def __init__(self,title, artist):
        super().__init__(title, artist)


#reads in file as dataframe

def read_music(file):
    df = pd.read_excel(file)
    master_list_of_songs= []
    # put music genre category (rnb, country, rock)
    for i in range(0,99):
        song = df.iloc[i]
        genre_label = song.loc['top genre']
        
    
        if "pop" in genre_label.lower():
            master_list_of_songs.append(Pop(song.loc['title'], song.loc['artist']))

        elif "hiphop" in genre_label.lower():
            master_list_of_songs.append(HipHop(song.loc['title'], song.loc['artist']))
        else:
            master_list_of_songs.append(OtherGenre(song.loc['title'], song.loc['artist']))
#return list of songs
    return master_list_of_songs