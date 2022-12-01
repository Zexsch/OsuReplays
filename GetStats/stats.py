class BeatmapStats:
    def __init__(self, data: dict[str:str]) -> None:
        self.new_data: dict[str, str | float] = {
            'circle_size': float(data['diff_size']),
            'overall_difficulty' :float(data['diff_overall']),
            'approach_rate': float(data['diff_approach']),
            'health': float(data['diff_drain']),
            'bpm': float(data['bpm']),
            'star_rating': round(float(data['difficultyrating']), 2),
            'name': data['title'],
            'artist': data['artist'],
            'difficulty_name': data['version'],
            'beatmapset_id': data['beatmapset_id']
        }
    
    def return_data(self) -> dict[str:str|float]:
        return self.new_data
    
    def __repr__(self) -> str:
        return str(self.new_data)


class PlayerStats:
    def __init__(self, data: dict[str:str | float]) -> None:
        self.new_data: dict[str, str | float] = {
            'user_id': int(data['user_id']),
            'username': data['username'],
            'total_pp': data['pp_raw'],
            'rank': data['pp_rank']
        }
        
    def return_data(self) -> dict[str:str]:
        return self.new_data
    
    def __repr__(self) -> str:
        return str(self.new_data)