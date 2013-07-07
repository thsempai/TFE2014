# -*- coding: utf-8 -*- 

from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2
from mutagen.easyid3 import EasyID3


def main():
    
    audio = MP3("test.mp3")
    audio["TIT2"] = TIT2(encoding=3, text=["MP3 ID3 TEST"])
    audio.save()

    audio = EasyID3("test.mp3")
    audio['title'] = "B-MAN of Craft-Craft"
    audio['artist'] = "Grungi!"
    audio.save()



if __name__ == "__main__":
	main()