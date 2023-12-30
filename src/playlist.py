
from src.channel import Channel


class PlayList:
    """  """
    def __init__(self, play_list_id):
        self.play_list_id = play_list_id
        self.channel = Channel.youtube.playlistItems().list(playlistId=self.play_list_id, part='id,snippet,contentDetails', maxResults=50).execute()

    def total_duration(self):
        pass

    def show_best_video(self):
        pass


pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
print(pl.channel)
