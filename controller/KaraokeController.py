from model.KaraokeModel import KaraokeModel
from view.KaraokeView import KaraokeView

class KaraokeController:
    def __init__(self):
        self.model = KaraokeModel()
        self.view = KaraokeView()

    def add_new_song(self):
        song_name, duration, singers = self.view.get_song_info()
        self.model.add_song(song_name, duration, singers)
        score = self.model.calculate_score(self.model.songs[-1])
        self.view.show_score(score)


