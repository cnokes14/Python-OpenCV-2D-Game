import cv2
import cvzone
from image_factory import *
from grid import *
from attack import *
from entity import *
from player_control import *
from enemy_control import *
from id_list import *

# Tag of the baseline frame, used as the background.
_back_scene = "PH"

# Function that gets the image position for an entity at a given x y coordinate.
def get_img_pos(x,y):
    return [245+x*126+y*30,200+y*102]

# Function that gets the status bar position for an entity at a given x y coordinate.
def get_bar_pos(x,y):
    img = get_img_pos(x,y)
    img[0] -= 20
    img[1] -= 20
    return img

# Sets and loads the baseline frame, loads a handful of other frames.
def init_scene(id : str, preloads : list):
    global _back_scene
    _back_scene = id
    preload_id(id)
    preload_id_lst(preloads)

# Selects a frame from a given list based on the current time.
#   Frames are selected assuming all animations play at 1fps.
def select_frame_time(t: int, frames : list):
    if frames is None or frames == []:
        return None
    l = len(frames)
    freq = 1000 / l
    tms = t % 1000
    return frames[int(tms / freq) % l]

# Selects a frame from a given list based on the placement of a value
#   on a scale between min and max.
def select_frame_scale(min : int, max : int, val : int, frames : list):
    diff = max - val
    if diff <= min:
        return frames[len(frames)-1]
    elif diff >= max:
        return frames[0]
    else:
        return frames[len(frames)-2 - int((len(frames)-2)*(diff / max))]

# Renders an individual entity. This is a simple process, but there are multiple paths.
#   1. Adds the entity frame (if one exists) to the current image, based on the current time.
#   2. If the entity is not a player or an enemy, exits.
#   3. If the entity is a player, it displays the health and stamina bars. Additionally, if the
#           entity is the active player, it displays the current attack cards and active player bars,
#           and if the entity is a player that is not the active player, it covers the card spaces.
#   4. If the entity is an enemy, it displays the health bar.
# All health and stamina bars are built based on scale. Cards and active player bars are built on time.
def render_entity(t: int, entity : list, back):
    frame = select_frame_time(t, entity[3])
    if frame is None:
        return
    cvzone.overlayPNG(back, frame, get_img_pos(entity[1], entity[2]))
    if is_player(entity[0]):
        if is_active_player(entity[0]):
            cvzone.overlayPNG(back, 
                              select_frame_time(t, get_frame_lst(TAG_ACTIVE_TEMP)[0]),
                              get_img_pos(entity[1], entity[2]))
            cards = get_active_cards()
            for card_idx in range(len(cards)):
                cvzone.overlayPNG(  back, 
                                    get_frame_lst(cards[card_idx])[0][card_idx],
                                    get_bar_pos(entity[1], entity[2]))
        else:
            cvzone.overlayPNG(back, 
                              select_frame_time(t, get_frame_lst(TAG_CARDS_NONE)[0]),
                              get_bar_pos(entity[1], entity[2]))
        
        cvzone.overlayPNG(  back, 
                            select_frame_scale(0,5000,get_attack_time(entity[0]) - t, get_frame_lst(TAG_PROGRESS)[0]), 
                            get_bar_pos(entity[1], entity[2]))
        cvzone.overlayPNG(  back, 
                            select_frame_scale(0,get_max_health(entity[0]),get_health(entity[0]), get_frame_lst(TAG_HEALTH)[0]), 
                            get_bar_pos(entity[1], entity[2]))
    elif is_enemy(entity[0]):
        cvzone.overlayPNG(  back, 
                            select_frame_scale(0,get_max_health(entity[0]),get_health(entity[0]), get_frame_lst(TAG_ENEMY_HP)[0]), 
                            get_bar_pos(entity[1], entity[2]))

# Renders a full image. This just gets a list of all active entities and attacks and renders them
#   each one at a time. Some notes:
#   1. The background is time selected, so it can move!
#   2. Items are rendered from 0,0 to 0,9 then 1,0 to 1,9, and so on. This means that entities
#       with a higher x value will be on top if they overlap with entities with lower x values,
#       and the same for the y coordinate.
#   3. Attacks are rendered after objects and characters. This ensures readability, if a player
#       is hiding a warning.
def render(t: int):
    back = select_frame_time(t, get_frame_lst(_back_scene)[0]).copy()
    entity_lst = []
    for y in range(GRID_Y_DIM):
        for x in range(GRID_X_DIM):
            occ = get_occupant(x,y)
            att = get_active_attacks(x,y,t)
            if occ != None and get_health(occ) > 0:
                entity_lst += [[occ, 
                                x, 
                                y, 
                                get_frame_lst(get_char_frame_id(occ))[0]]]
            if att != None and att != []:
                entity_lst += [[entry[ATTACK_GRID_ENTRY_IMAGE], 
                                x,
                                y,
                                get_frame_lst(entry[ATTACK_GRID_ENTRY_IMAGE])[0]] for entry in att]
    for entity in entity_lst:
        render_entity(t, entity, back)
    cv2.imshow("window", back)