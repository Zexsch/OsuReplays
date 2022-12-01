from pathlib import PurePath
from urllib.request import urlretrieve
from json import loads

from GetStats.player_info import fetch_player_info
from GetStats.stats import PlayerStats
from .edit_player_images import draw_player_stats

class ImageFetcher:
    def __init__(self, stats: dict[str:str|float], player_name: str) -> None:
        self.stats = stats
        self.player_name = player_name
        
        self.beatmap_url = f'https://assets.ppy.sh/beatmaps/{self.stats["beatmapset_id"]}/covers/cover.jpg'
        self.title = f'{self.player_name} - {self.stats["name"]}'
        
        self.PATH: PurePath = PurePath(__file__).parent
    
    def __repr__(self) -> str:
        return self.title
    
    def download_beatmap_image(self) -> None:
        filename = f'{self.PATH / "ThumbnailImages" / self.title}.jpg'
        urlretrieve(self.beatmap_url, filename)
    
    def fetch_player_image(self, index: int) -> None:
        player_info: list[bytes] = fetch_player_info()
        
        player_info[index] = loads(player_info[index].decode('utf-8'))
        stats = PlayerStats(player_info[index][0]).return_data()
        user_id = stats['user_id']

        self.player_url = f'http://s.ppy.sh/a/{user_id}'
        
        self.download_player_image()
        draw_player_stats(stats)
        
    def download_player_image(self) -> None:
        filename = f'{self.PATH / "PlayerImages" / self.player_name}.png'
        urlretrieve(self.player_url, filename)