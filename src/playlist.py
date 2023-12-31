
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

    def show_best_video(self):
        """ Возвращает ссылку на самое популярное видео из плейлиста """

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        video_response = Channel.youtube.videos().list(part='statistics',
                                                       id=','.join(video_ids)
                                                       ).execute()
        dict_ = video_response['items']

        like_count = 0
        vid_id = ''
        for item in range(4):

            if int(dict_[item]['statistics']['likeCount']) >= like_count:
                like_count = int(dict_[item]['statistics']['likeCount'])

                vid_id = dict_[item]['id']
        return f'https://youtu.be/{vid_id}'
