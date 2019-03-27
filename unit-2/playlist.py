from random import randint

class Playlist:
    def __init__(self):
        self.playlist = []

    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, id):
        for idx, song in enumerate(self.playlist):
            if song['id'] == id or song['Title'] == id:
                self.playlist.pop(idx)

    def shuffle_list(self):
        new_list = [" "] * len(self.playlist)
        list_length = len(self.playlist) -1

        for idx in self.playlist:
            random_idx = randint(0,list_length)
            if new_list[random_idx] == " ":
                new_list[random_idx] = idx
            else:
                while new_list[random_idx] != " ":
                    random_idx = randint(0,list_length)
                    if new_list[random_idx] == " ":
                        new_list[random_idx] = idx
                        break

        print(new_list)
        new_list = []
    def get_songs(self):
        for song in self.playlist:
            return f'{song["Title"]} by {song["Artist"]}'
    def size(self):
        length = len(self.playlist)
        return length


my_songs = Playlist()
my_songs.add_song({'id': 10,'Title': 'I don\'t know', 'Artist': 'Cardi B'})
my_songs.add_song({'id': 20, 'Title': 'The Flag Song', 'Artist': 'Unknown'})
my_songs.add_song({'id': 30, 'Title': 'ojwneojwenfwefwef', 'Artist': 'ngowengoiwnegNam'})
my_songs.add_song({'id': 40, 'Title': 'ojewneojwenfwefwef', 'Artist': 'ngowengofwefiwnegNam'})
my_songs.add_song({'id': 50, 'Title': 'ojwneojwefwewenfwefwef', 'Artist': 'ngwefwefowengoiwnegNam'})
#my_songs.remove_song('The Flag Song')

my_songs.shuffle_list()

