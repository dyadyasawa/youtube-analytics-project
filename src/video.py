from src.channel import Channel
class Video:
    def __init__(self, video_id: str) -> None:
        """ Экземпляр инициализируется id видео. Дальше все данные будут подтягиваться по API. """
        self.video_id = video_id
        self.channel = Channel.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()['items'][0]
        self.title = self.channel['snippet']['title']
        self.url = self.channel['snippet']['thumbnails']['default']['url']
        self.total_view_count = self.channel['statistics']['viewCount']
        self.likes_count = self.channel['statistics']['likeCount']
    def __str__(self):
        """ Реализует вывод необходимой информации по экземпляру класса. """
        return f'{self.title}'

class PLVideo(Video):
    def __init__(self, video_id, play_list_id):
        """ Наследуется от класса Video. Id видео заимствуется у родительского класса. Экземпляр инициализируется id плейлиста. Дальше все данные будут подтягиваться по API. """
        super().__init__(video_id)
        self.play_list_id = play_list_id
        self.channel = Channel.youtube.videos().list(part='snippet, statistics, contentDetails, topicDetails', id=video_id).execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.url = self.channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']
        self.like_count = self.channel['items'][0]['statistics']['likeCount']
    def __str__(self):
        """ Реализует вывод необходимой информации по экземпляру класса. """
        return f'{self.title}'
