class Song:
    def __init__(self, artist, name, album, position, year, duration):
        self.artist = artist
        self.name = name
        self.album = album
        self.position = position
        self.year = year
        self.duration = duration
    def __repr__(self):
        song = self.artist + "\t" + self.name + "\t" + self.album + "\t" + self.position + "\t" + self.year + "\t" + self.duration
        return str(song)
    def __lt__(self, other):
        if self.artist < other.artist:
            return True
        if self.artist == other.artist and self.name < other.name:
            return True
        return False

# Import songs from file & return them as tsv
def import_songs(file_name):
    input_file = open(file_name, "r")
    lines = input_file.readlines()
    songs = []
    for line in lines:
        name, artist, album, position, year, duration = line.split("\t")
        songs.append(Song(artist, name, album, position, year, duration))
    return songs
#test
#print(import_songs("./songs.txt"))


# Export list of songs & write them into file
def export_songs(songs_as_list, file_name):
    input_file = open(file_name, "a")    #append mode
    for element in songs_as_list:
        element = str("\n" + element)
        print(element)
        input_file.write(element)
    input_file.close()
#test
#export_songs([list of songs], ./songs.txt)


# Shuffle
def shuffle_song(songs):
    from random import shuffle
    shuffle(songs)
    return songs
#test
#print(shuffle_song([list of songs]))


# Most popular artist
def most_popular(file_name):
    songs_list = import_songs(file_name)
    artist_list = []
    for song in songs_list:
        artist_list.append(song.artist)
        dict = {}
        counter = 1
        for i in artist_list:
            if i not in dict:
                counter = 1
                dict[i] = counter
            else:
                counter += 1
                dict[i] = counter
    pop_value = max(dict.values())
    return dict.fromkeys()


print(most_popular('./songs2.txt'))






