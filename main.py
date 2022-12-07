from json import loads
from os import listdir
from os import remove
from pathlib import PurePath
from shutil import move

from GetStats.request_info import fetch_beatmap_info
from GetStats.stats import BeatmapStats
from Image.get_image import ImageFetcher
from Image.edit_beatmap_images import draw_stats
from Config.create_dirs import create_image_dirs
from Config.create_dirs import create_replay_dirs
from Config.threads import start_thread

def main() -> None:
    print('Started Operation.')
    start_thread()
    create_image_dirs()
    create_replay_dirs()
    
    info = fetch_beatmap_info()
    data: list[bytes] = info[0]
    player_names: list[str] = info[1]
        
    for i in range(len(data)):
        data[i] = loads(data[i].decode('utf-8'))
        stats = BeatmapStats(data[i][0]).return_data()
        fetcher = ImageFetcher(stats=stats, player_name=player_names[i])
        fetcher.download_beatmap_image()
        fetcher.fetch_player_image(i)
        fetcher.download_player_image()
        
        draw_stats(stats=stats, player_name=player_names[i])

    PATH = PurePath(__file__).parent
    
    beatmap_files: list[str] = [f for f in listdir(path=str(PATH / 'Replays'))]
    move_path = PATH / 'MovedReplays'
    for i in range(len(beatmap_files)):
        move(PATH / 'Replays' / beatmap_files[i], move_path)
        
    player_files: list[str] = [f for f in listdir(path=str(PATH / 'Image' / 'PlayerImages'))]
    for i in player_files:
        remove(str(PATH / 'Image' / 'PlayerImages' / i))
        
    print('Finished Operation.')
    

if __name__ == '__main__':
    main()