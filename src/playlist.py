
import isodate
import datetime
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

        @property
        def total_duration(self):
            """ Суммарная длительность видеороликов из плейлиста """

            # Id видеороликов из плейлиста
            video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]

            # Статистика видео по его id
            video_response = Channel.youtube.videos().list(part='contentDetails,statistics',
                                                           id=','.join(video_ids)
                                                           ).execute()

            total_time = datetime.timedelta(0)
            for video in video_response['items']:
                # YouTube video duration is in ISO 8601 format
                iso_8601_duration = video['contentDetails']['duration']
                duration = isodate.parse_duration(iso_8601_duration)
                total_time += duration
            return total_time
