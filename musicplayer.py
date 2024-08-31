import random
from playsound import playsound

class Audio:
    def __init__(self, title, url, genre):
        self.title = title
        self.url = url
        self.genre = genre
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)

    def get_average_rating(self):
        if len(self.ratings) == 0:
            return 0
        return sum(self.ratings) / len(self.ratings)

class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.audios = []
        self.ratings = []

    def add_audio(self, audio):
        self.audios.append(audio)

    def search_audio(self, audio_name):
        for audio in self.audios:
            if audio.title.lower() == audio_name.lower():
                return audio
        return None

    def add_rating(self, rating):
        self.ratings.append(rating)

    def get_average_rating(self):
        if len(self.ratings) == 0:
            return 0
        return sum(self.ratings) / len(self.ratings)

class User:
    def __init__(self, username):
        self.username = username
        self.playlists = []

    def create_playlist(self, name, genre):
        playlist = Playlist(name, genre)
        self.playlists.append(playlist)
        return playlist

    def search_playlist(self, playlist_name):
        for playlist in self.playlists:
            if playlist.name.lower() == playlist_name.lower():
                return playlist
        return None

    def rate_playlist(self, playlist, rating):
        playlist.add_rating(rating)

    def rate_audio(self, audio, rating):
        audio.add_rating(rating)

# Example Usage
if __name__ == "__main__":
    # Create 3 users
    users = [User(f"User_{i}") for i in range(1, 4)]

    # Create some playlists and audios
    playlist1 = users[0].create_playlist("Chill Vibes", "Chill")
    playlist2 = users[1].create_playlist("Workout Jams", "Workout")

    audio1 = Audio("Ocean Waves", "https://example.com/oceanwaves.mp3", "Chill")
    audio2 = Audio("Rock Anthem", "https://example.com/rockanthem.mp3", "Workout")

    playlist1.add_audio(audio1)
    playlist2.add_audio(audio2)

    # Randomly rate playlists and audios
    for user in users:
        random_rating = random.randint(1, 5)
        user.rate_playlist(playlist1, random_rating)
        user.rate_audio(audio1, random_rating)

        random_rating = random.randint(1, 5)
        user.rate_playlist(playlist2, random_rating)
        user.rate_audio(audio2, random_rating)

    # Display average ratings
    print(f"Playlist 1 ('Chill Vibes') Average Rating: {playlist1.get_average_rating()}")
    print(f"Playlist 2 ('Workout Jams') Average Rating: {playlist2.get_average_rating()}")

    print(f"Audio 1 ('Ocean Waves') Average Rating: {audio1.get_average_rating()}")
    print(f"Audio 2 ('Rock Anthem') Average Rating: {audio2.get_average_rating()}")
