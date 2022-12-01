from pathlib import PurePath
from os import listdir
from shutil import move

class BeatmapFetcher:
    def __init__(self) -> None:
        self.PATH: PurePath = PurePath(__file__).parent.parent
        self.REPLAY_PATH: PurePath = self.PATH / 'Replays'
        self.beatmap_files: list[str] = []
        self.data: list[str] = []
        self.beatmap_files = [f for f in listdir(path=self.REPLAY_PATH)]
                
    def move_replay(self) -> None:
        self.move_path = self.PATH / 'MovedReplays'
        for i in range(len(self.beatmap_files)):
            move(self.REPLAY_PATH / self.beatmap_files[i], self.move_path)
            
    def get_beatmap_hash(self) -> str:
        for i in range(len(self.beatmap_files)):
            with open(self.REPLAY_PATH / self.beatmap_files[i], 'r', encoding="iso-8859-1") as f:
                content: list[str] = [line for line in f]
                self.data.append(content[0].split())
        
        #  self.move_replay()
    
    def return_data(self) -> list[str]:
        self.get_beatmap_hash()
        return self.data