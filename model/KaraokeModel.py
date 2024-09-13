from controller.database import KaraokeDatabase

class KaraokeModel:
    def __init__(self):
        self.db = KaraokeDatabase()
        self.songs = []

    def add_song(self, song_name, duration, singers):
        self.db.add_song(song_name, duration, singers)
        self.songs.append({
            "song_name": song_name,
            "duration": duration,
            "singers": singers
        })

    def calculate_score(self, song):
        singers = song["singers"]
        if len(singers) == 1:
            return sum([s["duration"] for s in self.songs]) % 100
        elif len(singers) == 2:
            return (song["duration"] * sum(len(s) for s in singers)) % 100
        elif len(singers) == 3:
            prev_singers_length = sum(len(s) for s in [s for song in self.songs for s in song["singers"]])
            return (prev_singers_length * sum(len(s) for s in singers)) % 100
        return 0
