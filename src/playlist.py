
from src.channel import Channel


class PlayList:
    """  """
    def __init__(self, play_list_id):
        self.play_list_id = play_list_id
        self.channel = Channel.youtube.playlists().list(id=self.play_list_id, part='contentDetails,snippet', maxResults=50).execute()
        self.title = self.channel['items'][0]['snippet']['title']
    def total_duration(self):
        pass

    def show_best_video(self):
        pass


pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
print(pl.title)
