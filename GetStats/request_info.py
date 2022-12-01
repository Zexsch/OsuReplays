from requests import get
from Config.config import ACCESS_KEY
from .beatmap import BeatmapFetcher

def fetch_beatmap_info() -> list[str | int | float]:
    data = BeatmapFetcher().return_data()
    content: list[dict[str:str]] = []
    player_names: list[str] = []
    for i in range(len(data)):
        url = f'https://osu.ppy.sh/api/get_beatmaps?k={ACCESS_KEY}&h={data[i][1]}'
        
        response = get(url)
        content.append(response.content)
        player_names.append(str(data[i][2])[1:])
    
    returned = [content, player_names]
    return returned