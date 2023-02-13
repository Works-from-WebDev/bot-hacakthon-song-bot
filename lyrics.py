import lyricsgenius
from keys import API_KEY
from all_songs import singers
import random
import re


def random_song():
    keys = list(singers)
    artist = random.choice(keys)
    song = random.choice(singers[artist])
    ly = lyrics(artist, song)
    ly = re.sub("\n", " ", ly, )
    ly = re.sub(r"(.*)(Lyrics)", "", ly)
    ly = re.sub(r'[^\w\s]', '', ly)
    ly = ly.split()
    return [song, artist, ly[:-4]]


def lyrics(artist, song):
    genius = lyricsgenius.Genius(API_KEY)
    genius.verbose = False
    genius.remove_section_headers = True
    song = genius.search_song(song, artist)
    return song.lyrics
