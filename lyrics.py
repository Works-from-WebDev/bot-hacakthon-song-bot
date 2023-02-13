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
    ly = ly.split()
    result = []
    inside = 0
    #
    # for i, x in enumerate(list(ly)):
    #     if "Chorus" in list(ly)[i + 1]:
    #         ly = "".join(list(ly)[i + 1:])

    # ly = re.sub(r'\[(.*?)\]', "", ly)

    return [song, artist, ly]


def lyrics(artist, song):
    genius = lyricsgenius.Genius(bot_settings.API_KEY)
    genius.verbose = False
    genius.remove_section_headers = True
    song = genius.search_song(song, artist)
    return song.lyrics



# print(lyrics('Bury a Friend', 'Billie Eilish'))

print(random_song())
