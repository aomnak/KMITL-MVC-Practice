class KaraokeView:
    def get_song_info(self):
        song_name = input("Enter song name: ")
        duration = int(input("Enter song duration in seconds: "))
        singers = input("Enter singers (comma separated, max 3): ").split(",")
        return song_name, duration, singers

    def show_score(self, score):
        print(f"Score for the song: {score}")
