# -*- coding: utf-8 -*- 

from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TXXX, TPE1
from mutagen.easyid3 import EasyID3


def main():
    
    audio = MP3("test.mp3")
    audio["TIT2"] = TIT2(encoding=3, text=["MP3 ID3 TEST 666"])
    audio["TPE1"] = TPE1(encoding=3, text=["Grungi"])
    audio["TXXX"] = TXXX(encoding=3, desc="ankhfire::ambiance", text=["Gore!!!"])
    audio["QuodLibet"] = TXXX(encoding=3, desc="QuodLibet::test", text=["Yeah!!"])
    audio.save()


    for a in audio:
        print a


if __name__ == "__main__":
	main()