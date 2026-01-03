from common_util import *
from id_list import *

# An entity is any player, enemy, or object that exists on the board.
#   An entity is defined by its various entries:
#       x position
#       y position
#       type (player, enemy, object, or invalid)
#       tag used to select rendered frames
#       attributes, currently unused
#       name
#       attacks (or possible cards, for players)
#       time when eligible for next attack
#       time when eligible for next move
#       minimum time before move eligibility
#       maximum time before move eligibility
#       health
#       max health
#       sound map dictionary of triggers to sound tags
_ENTITY_X = "pos_x"
_ENTITY_Y = "pos_y"
_ENTITY_TYPE = "etype"
_ENTITY_TYPE_PLAYER = "P"
_ENTITY_TYPE_ENEMY = "E"
_ENTITY_TYPE_OBJECT = "O"
_ENTITY_TYPE_INVALID = "I"
_ENTITY_CHAR_FRAME_ID = "char_frame_id"
_ENTITY_ATTRIBUTE_LST = "attribute_lst"
_ENTITY_NAME = "name"
_ENTITY_PLAYER_CARDS = "attacks"
_ENTITY_ENEMY_ATTACKS = "attacks"
_ENTITY_NEXT_ATTACK = "next_attack"
_ENTITY_NEXT_MOVE = "next_move"
_ENTITY_MOVE_TIME_MIN = "move_time_min"
_ENTITY_MOVE_TIME_MAX = "move_time_max"
_ENTITY_HEALTH = "hp"
_ENTITY_MAX_HEALTH = "hp_max"
_ENTITY_SOUNDS = "sounds" # a dict of lists

_EMPTY_ENTITY = {_ENTITY_NAME           : "PH_ENTITY_NAME",
                 _ENTITY_X              : -1, 
                 _ENTITY_Y              : -1,
                 _ENTITY_TYPE           : _ENTITY_TYPE_INVALID,
                 _ENTITY_CHAR_FRAME_ID  : "",
                 _ENTITY_ATTRIBUTE_LST  : [],
                 _ENTITY_ENEMY_ATTACKS  : [],
                 _ENTITY_NEXT_ATTACK    : -1,
                 _ENTITY_NEXT_MOVE      : -1,
                 _ENTITY_MOVE_TIME_MIN  : -1,
                 _ENTITY_MOVE_TIME_MAX  : -1,
                 _ENTITY_HEALTH         : -1,
                 _ENTITY_MAX_HEALTH     : -1,
                 _ENTITY_SOUNDS         : dict()}

# This list checks what entities are currently active, alive or dead.
_entity_lst = dict()

# This function creates a simple entity based on coordinates, name, type, and image.
def _create_entity(name : str, 
                   x : int, 
                   y : int, 
                   etype : str, 
                   frame_id : str):
    if id in _entity_lst or \
        (etype != _ENTITY_TYPE_PLAYER and
         etype != _ENTITY_TYPE_ENEMY and
         etype != _ENTITY_TYPE_OBJECT):
            return False
    entity = _EMPTY_ENTITY.copy()
    entity[_ENTITY_NAME] = name; entity[_ENTITY_X] = x; entity[_ENTITY_Y] = y
    entity[_ENTITY_TYPE] = etype; entity[_ENTITY_CHAR_FRAME_ID] = frame_id
    _entity_lst[name] = entity

# This function gives an entity various attributes relevant only to living entities.
def _initialize_live(id : str,
                     hp : int,
                     attacks : list,
                     attributes : list,
                     move_min : int,
                     move_max : int):
    entity = _entity_lst[id]
    entity[_ENTITY_HEALTH]           = hp
    entity[_ENTITY_MAX_HEALTH]       = hp
    entity[_ENTITY_ENEMY_ATTACKS]    = attacks
    entity[_ENTITY_ATTRIBUTE_LST]    = attributes
    entity[_ENTITY_NEXT_ATTACK]      = 0
    entity[_ENTITY_NEXT_MOVE]        = 0
    entity[_ENTITY_MOVE_TIME_MIN]    = move_min
    entity[_ENTITY_MOVE_TIME_MAX]    = move_max

# This function passes a sound map (i.e., a dictionary of triggers to sound tags) to an entity
def _initialize_soundmap(id : str, sound_dict : dict):
    entity = _entity_lst[id]
    entity[_ENTITY_SOUNDS] = sound_dict

# This function creates a player entity. An enemy entity has a variable
#   move time determined by randomly selecting within the min-max range,
#   and has the enemy entity etype.
def create_enemy(name       : str, 
                 x          : int, 
                 y          : int,
                 frame_id   : str,
                 hp         : int  = 1,
                 attacks    : list = [],
                 attributes : list = [],
                 move_min   : int  = 250,
                 move_max   : int  = 500,
                 sound_dict : dict = dict()):
    _create_entity(name=name, 
                   x=x, 
                   y=y, 
                   etype=_ENTITY_TYPE_ENEMY,
                   frame_id=frame_id)
    _initialize_live(id=name,
                     hp=hp,
                     attacks=attacks,
                     attributes=attributes,
                     move_min=move_min,
                     move_max=move_max)
    _initialize_soundmap(id=name,
                         sound_dict=sound_dict)

# This function creates a player entity. A player entity
#   has a constant move time (rather than a random range)
#   and has the player entity etype
def create_player(name       : str, 
                  x          : int, 
                  y          : int,
                  frame_id   : str,
                  hp         : int  = 1,
                  cards      : list = [],
                  attributes : list = [],
                  move       : int  = 500,
                  sound_dict : dict = dict()):
    _create_entity(name=name, 
                   x=x, 
                   y=y, 
                   etype=_ENTITY_TYPE_PLAYER,
                   frame_id=frame_id)
    _initialize_live(id=name,
                     hp=hp,
                     attacks=cards,
                     attributes=attributes,
                     move_min=move,
                     move_max=move)
    _initialize_soundmap(id=name,
                         sound_dict=sound_dict)

# This function checks if an entity is a player or enemy (i.e., living)
def _is_living(id : str):
    return (id in _entity_lst and \
        (_entity_lst[id][_ENTITY_TYPE] == _ENTITY_TYPE_PLAYER or 
         _entity_lst[id][_ENTITY_TYPE] == _ENTITY_TYPE_ENEMY))

# This function returns true if a given entity is eligible to attack, and false otherwise.
def attack_time_valid(id : str, t : int):
    return _is_living(id=id) and _entity_lst[id][_ENTITY_NEXT_ATTACK] <= t

# This function returns true if a given entity is eligible to move, and false otherwise.
def move_time_valid(id : str, t : int):
    return _is_living(id=id) and _entity_lst[id][_ENTITY_NEXT_MOVE] <= t

# This function gets the time at which a living entity may next attack
def get_attack_time(id : str):
    if not _is_living(id=id):
        return None
    return _entity_lst[id][_ENTITY_NEXT_ATTACK]

# This function gets the time at which a living entity may next move
def get_move_time(id : str):
    if not _is_living(id=id):
        return None
    return _entity_lst[id][_ENTITY_NEXT_MOVE]

# This function updates the time at which an entity may attack next. Time is not
#   randomized, and the input time is the new attack time.
def update_attack_time(id : str, tnew : int):
    if not _is_living(id):
        return False
    _entity_lst[id][_ENTITY_NEXT_ATTACK] = tnew
    return True

# This function updates the time at which an entity may move next. Time is randomized,
#   and the input time is the current time.
def update_move_time(id : str, tnow : int):
    if not _is_living(id):
        return False
    _entity_lst[id][_ENTITY_NEXT_MOVE] = tnow + rintrange(_entity_lst[id][_ENTITY_MOVE_TIME_MIN], 
                                                          _entity_lst[id][_ENTITY_MOVE_TIME_MAX])
    return True

# This function updates the position of an entity to a given x,y coordinate pair.
def update_position(id : str, x : int, y : int):
    if not _is_living(id) or \
        _entity_lst[id][_ENTITY_MOVE_TIME_MIN] < 0 or \
        _entity_lst[id][_ENTITY_MOVE_TIME_MAX] < 0:
            return False
    _entity_lst[id][_ENTITY_X] = x; _entity_lst[id][_ENTITY_Y] = y
    return True

# This function damages an entity, if it can be damaged.
def damage_entity(id : str, damage : int):
    if not _is_living(id=id):
        return False
    # TODO: check against attributes here
    _entity_lst[id][_ENTITY_HEALTH] -= damage
    return True

# This function gets the x,y coordinate pair of an entity.
def get_char_pos(id : str):
    if id not in _entity_lst:
        return None,None
    return _entity_lst[id][_ENTITY_X], _entity_lst[id][_ENTITY_Y]

# This function gets the tag of the images used to display the entity.
def get_char_frame_id(id : str):
    if id not in _entity_lst:
        return None
    return _entity_lst[id][_ENTITY_CHAR_FRAME_ID]

# This function gets the possible attacks usable by an entity.
def get_char_attacks(id : str):
    if id not in _entity_lst:
        return None
    return _entity_lst[id][_ENTITY_ENEMY_ATTACKS]

# This function gets the health of an entity.
def get_health(id : str):
    if id not in _entity_lst:
        return None
    return _entity_lst[id][_ENTITY_HEALTH]

# This function gets the maximum health of an entity.
def get_max_health(id : str):
    if id not in _entity_lst:
        return None
    return _entity_lst[id][_ENTITY_MAX_HEALTH]

# This function gets the tag of a random footstep for an entity.
def get_entity_footstep_random(id : str):
    if id not in _entity_lst or \
       TAG_SOUND_CATEGORY_FOOTSTEPS not in _entity_lst[id][_ENTITY_SOUNDS] or \
       len(_entity_lst[id][_ENTITY_SOUNDS][TAG_SOUND_CATEGORY_FOOTSTEPS]) <= 0:
        return None
    return random.sample(_entity_lst[id][_ENTITY_SOUNDS][TAG_SOUND_CATEGORY_FOOTSTEPS], 1)[0]