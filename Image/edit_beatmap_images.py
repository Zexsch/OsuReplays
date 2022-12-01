from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from pathlib import PurePath
from os import remove

def text_draw(draw: ImageDraw.Draw, x: int, y: int, 
              string: str, font: ImageFont.truetype) -> None:
    BLACK = (0, 0, 0)
    # Text Outline
    draw.text((x-1,y-1), string, font=font, fill=BLACK)
    draw.text((x+1,y-1), string, font=font, fill=BLACK)
    draw.text((x-1,y+1), string, font=font, fill=BLACK)
    draw.text((x+1,y+1), string, font=font, fill=BLACK)
    
    # Text
    draw.text((x,y), string, font=font)

def draw_stats(stats: dict[str,str|float], player_name: str) -> None:
    PATH = PurePath(__file__).parent
    FONTPATH = PATH / 'font' / 'Swiss721BlackBT.ttf'
    image_name = f'{player_name} - {stats["name"]}.jpg'
    
    big_font = ImageFont.truetype(font=str(FONTPATH), size=40)
    medium_font = ImageFont.truetype(font=str(FONTPATH), size=30)
    small_font = ImageFont.truetype(font=str(FONTPATH), size=20)
    
    imgpath = PATH / 'ThumbnailImages' / image_name
    
    image = Image.open(str(imgpath))
    draw = ImageDraw.Draw(image)
    
    WIDTH, HEIGHT = image.size
    
    # TEXT
    # Map
    title_string = f'{stats["artist"]} - {stats["name"]}'
    if len(title_string) > 45:
        if len(stats["artist"]) > 30:
            text_draw(draw, 10, 10, str(stats["artist"]), medium_font)  # Artist
        else:
            text_draw(draw, 10, 10, str(stats["artist"]), big_font)  # Artist
        
        if len(stats["name"]) > 45:
            text_draw(draw, 10, 60, str(stats["name"]), medium_font)  # Title
        else:
            text_draw(draw, 10, 60, str(stats["name"]), big_font)  # Title
        
        text_draw(draw, 10, 100, stats['difficulty_name'], medium_font)  # Difficulty name
    else:
        text_draw(draw, 10, 10, f'{stats["artist"]} - {stats["name"]}', big_font)  # Artist and title
        text_draw(draw, 10, 60, stats['difficulty_name'], medium_font)  # Difficulty name
    
    
    
    # Beatmap Stats
    # Top right
    text_draw(draw, WIDTH-130, 10, f'{stats["star_rating"]}*', big_font)  # Star rating
    text_draw(draw, WIDTH-200, 70, f'BPM: {str(int(stats["bpm"]))}', medium_font)  # BPM
    
    # Bottom
    text_draw(draw, 10, HEIGHT-60, f'OD: {str(stats["overall_difficulty"])}', big_font)  # OD
    text_draw(draw, 200, HEIGHT-60, f'AR: {str(stats["approach_rate"])}', big_font)  # AR
    text_draw(draw, 400, HEIGHT-60, f'CS: {str(stats["circle_size"])}', big_font)  # CS
    text_draw(draw, 600, HEIGHT-60, f'HP: {str(stats["health"])}', big_font)  # HP
    
    image.save(str(PATH.parent / 'ImageOutput' / 'Beatmap' / image_name))
    remove(str(imgpath))