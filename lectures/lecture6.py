# classes

class Song:
    def __init__(self, artist, name):
        self.artist = artist
        self.name = name

    def __repr__(self):
        song = self.artist + " with song: " + self.name
        return song
    def __lt__(self, other):
        if self.artist < other.artist:
            return True
        if self.artist == other.artist and self.name < other.name:
            return True
        return False

input_file = open("/home/daniil/python-course/songs_shuffled.txt", "r")
lines = input_file.readlines()

songs = []
n = int(lines[0])
for i in range(n):
    artist, name = lines[1 + i][:-1].split("-")
    songs.append(Song(artist, name))

def filter_songs(songs, word):
    correct_list = []
    word = word.lower()
    for song in songs:
        if word in song.artist.lower() or word in song.name.lower():
            correct_list.append(song)
    return correct_list

for song in sorted(filter_songs(songs, " ")):
    print(song)

input_file.close()