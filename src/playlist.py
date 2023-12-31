
from src.channel import Channel


class PlayList:
    """ Класс для плейлиста  """
    def __init__(self, play_list_id):
        self.play_list_id = play_list_id

        # Данные по плейлистам.
        self.info = Channel.youtube.playlists().list(id=self.play_list_id, part='snippet',
                                                     maxResults=50
                                                     ).execute()

        # Данные по видеороликам в плейлистах.
        self.playlist_videos = Channel.youtube.playlistItems().list(playlistId=self.play_list_id,
                                                                    part='contentDetails',
                                                                    maxResults=50,
                                                                    ).execute()

        self.title = self.info['items'][0]['snippet']['localized']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.play_list_id}'
