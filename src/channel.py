
import json
import os
from googleapiclient.discovery import build

api_key = os.getenv("YT_API_KEY")

class Channel:
    """Класс для ютуб-канала"""

    youtube = build('youtube', 'v3', developerKey=api_key)


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = Channel.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['localized']['title']
        self.description = self.channel['items'][0]['snippet']['localized']['description']
        self.url = self.channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscribers_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.total_view_count = self.channel['items'][0]['statistics']['viewCount']


    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_id = 'UCwHL6WHUarjGfUM_586me8w'  # HighLoad Channel
        channel = Channel.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        Channel.printj(channel)
