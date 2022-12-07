from pathlib import PurePath
from os import path, makedirs


def create_image_dirs() -> None:
    PATH = PurePath(__file__).parent.parent # Main dir
    image_output_path = PATH / 'ImageOutput'
    
    if not path.exists(str(image_output_path)):
        makedirs(str(image_output_path))
        makedirs(str(image_output_path / 'Beatmap'))
        makedirs(str(image_output_path / 'Player'))
    
    image_input_path = PATH / 'Image'
    
    if not path.exists(str(image_input_path / 'PlayerImages')):
        makedirs(str(image_input_path / 'PlayerImages'))
    
    if not path.exists(str(image_input_path / 'ThumbnailImages')):
        makedirs(str(image_input_path / 'ThumbnailImages'))


def create_replay_dirs() -> None:
    PATH = PurePath(__file__).parent.parent # Main dir
    replay_output_path = PATH / 'Replays'
    
    if not path.exists(str(replay_output_path)):
        makedirs(str(replay_output_path))
    
    moved_replay_output_path = PATH / 'MovedReplays'
    
    if not path.exists(str(moved_replay_output_path)):
        makedirs(str(moved_replay_output_path))

