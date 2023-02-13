import lyricsgenius
import bot_settings
from all_songs import all_singers
import random
import re


def random_song(song_type):
    if song_type == "EN":
        index = 0
        singers = all_singers[index]
    elif song_type == "HE":
        index = 1
        singers = all_singers[index]
    else:
        singers = all_singers[0] | all_singers[1]
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
# print(random_song('BOTH'))
