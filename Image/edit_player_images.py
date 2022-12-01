from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from pathlib import PurePath

from .edit_beatmap_images import text_draw


def draw_player_stats(stats: dict[str,str]) -> None:
    PATH = PurePath(__file__).parent
    FONTPATH = PATH / 'font' / 'Swiss721BlackBT.ttf'
    image_name = stats['username'] + '.png'
    
    imgpath = PATH / 'PlayerImages' / image_name
    save_path = PATH.parent / 'ImageOutput' / 'Player' / image_name
    
    big_font = ImageFont.truetype(font=str(FONTPATH), size=80)
    medium_font = ImageFont.truetype(font=str(FONTPATH), size=60)
    small_font = ImageFont.truetype(font=str(FONTPATH), size=40)
    
    image = Image.open(str(imgpath))
    image = image.resize((200,200), Image.Resampling.LANCZOS)
    
    WIDTH, HEIGHT = image.size
    
    background_image = Image.new(mode='RGBA', size=(WIDTH*3, HEIGHT))
    background_image.save(str(save_path))
    
    background_image = Image.open(str(save_path))
    background_image.paste(image, (int(WIDTH*2), 0))
    
    draw = ImageDraw.Draw(background_image)
    
    text_draw(draw, 10, 10, stats['username'], big_font)  # Username
    
    string = f'#{stats["rank"]} - {int(float(stats["total_pp"]))}pp'
    
    if len(string) < 12:
        text_draw(draw, 10, 140, string, medium_font) # PP and Rank
    else:
        text_draw(draw, 10, 140, string, small_font) # PP and Rank
    
    background_image.save(str(save_path))