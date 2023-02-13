import lyricsgenius
import keys
from all_songs import singers
import random
import re


def random_song():
    keyss = list(singers)
    artist = random.choice(keyss)
    song = random.choice(singers[artist])
    ly = lyrics(artist, song)
    ly = re.sub("\n", " ", ly, )
    ly = re.sub(r"(.*)(Lyrics)", "", ly)
    ly = ly.split()


    return [song, artist, ly]


def lyrics(artist, song):
    genius = lyricsgenius.Genius(keys.API_KEY)
    genius.verbose = False
    genius.remove_section_headers = True
    song = genius.search_song(song, artist)
    return song.lyrics



# print(lyrics('Bury a Friend', 'Billie Eilish'))

