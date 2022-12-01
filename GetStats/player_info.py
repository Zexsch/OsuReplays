from requests import get

from Config.config import ACCESS_KEY
from .request_info import fetch_beatmap_info

def fetch_player_info() -> dict[str,str]:
    player_names = fetch_beatmap_info()[1]
    player_info = []
    
    for i in range(len(player_names)):
        url = f'https://osu.ppy.sh/api/get_user?k={ACCESS_KEY}&u={player_names[i]}'
        response = get(url)
        player_info.append(response.content)
    
    return player_info