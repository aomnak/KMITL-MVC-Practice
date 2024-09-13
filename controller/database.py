import json
import os

class KaraokeDatabase:
    def __init__(self, db_file="karaoke_data.json"):
        self.db_file = db_file
        if not os.path.exists(self.db_file):
            self._create_empty_db()

    def _create_empty_db(self):
        with open(self.db_file, 'w') as f:
            json.dump({"songs": []}, f)

    def load_data(self):
        with open(self.db_file, 'r') as f:
            return json.load(f)

    def save_data(self, data):
        with open(self.db_file, 'w') as f:
            json.dump(data, f, indent=4)

    def add_song(self, song_name, duration, singers):
        data = self.load_data()
        data['songs'].append({
            "song_name": song_name,
            "duration": duration,
            "singers": singers
        })
        self.save_data(data)
