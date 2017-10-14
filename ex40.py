class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy Birthday to you",
                   "I don't want to be sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

song2 = ["Call me maybe", "Here's my number!"]

call_me = Song(song2)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

call_me.sing_me_a_song()
