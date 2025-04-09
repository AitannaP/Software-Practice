from music import  Music, HipHop, Pop, OtherGenre, read_music
import pandas as pd
from pathlib import Path
from playlist import Playlist
import random 


#read in data with genre and put it into type music
file = Path('./Spotify2010s_100songs.xlsx')


#add file > df > and make types of music throuh there
temp = read_music(file)

#print list of all songs
ipod = Playlist(temp)
# ipod.print_all_songs()


#make a playlist 
# ipod.shuffle()
temp = random.sample(ipod.list_of_music, 25)

for index in  range(0,len(temp)):
    print( temp[index].title, temp[index].artist, type(temp[index]))


    #dont add duplicates