from GetStats.request_info import fetch_beatmap_info
from GetStats.stats import Stats
from Image.get_image import ImageFetcher
from json import loads

def main() -> None:
    info = fetch_beatmap_info()
    data: list[bytes] = info[0]
    player_names: list[str] = info[1]

    for i in range(len(data)):
        data[i] = loads(data[i].decode('utf-8'))
        stats = Stats(data[i][0]).return_data()
        print(repr(ImageFetcher(stats=stats, player_name=player_names[i])))
        


if __name__ == '__main__':
    main()