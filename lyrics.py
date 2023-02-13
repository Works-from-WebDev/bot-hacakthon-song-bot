import lyricsgenius
import bot_settings
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
    genius = lyricsgenius.Genius(bot_settings.API_KEY)
    genius.verbose = False
    genius.remove_section_headers = True
    song = genius.search_song(song, artist)
    return song.lyrics



# print(lyrics("שיר בבוקר בבוקר", "שלמה ארצי"))

print(random_song())
