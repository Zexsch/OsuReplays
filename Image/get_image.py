from requests import get

class ImageFetcher:
    def __init__(self, stats: dict[str:str|float], player_name: str) -> None:
        self.url = f'https://assets.ppy.sh/beatmaps/{stats["beatmapset_id"]}/covers/cover.jpg'
        self.title = f'{player_name} - {stats["name"]}'
    
    def __repr__(self) -> str:
        return self.title
    
    def download_image(self) -> None:
        pass
    