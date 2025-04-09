import music
import random as rand

class Playlist:
    # master_list_of_music= []


    #init playlist with list of music
    def __init__(self, list_of_music):
        self.list_of_music = list_of_music
        
    def print_all_songs(self):

        for index in range ( 0,99):
            print( self.list_of_music[index].title, self.list_of_music[index].artist, type(self.list_of_music[index]))

    #def make playlist with 10 pop 10 hip hop an 5 other genre/ 25 songs
    def shuffle(self):
  
        shuffled_playist =[]
        # rand.shuffle(self.list_of_music,25)
        return rand.shuffle(self.list_of_music,25)

    #check for duplicates
    def check_for_duplicates(self):
        pass


    