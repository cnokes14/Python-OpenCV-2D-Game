from entity_control import *

_player_list         = []
_active_character_id = None
_active_cards        = None

# This function creates a player entity, pushes it to the grid, and adds it
#   to the list of players. Additionally, if there is no active player, the new
#   player becomes the active player.
def add_player( name       : str, 
                x          : int, 
                y          : int,
                frame_id   : str,
                hp         : int  = 1,
                cards      : list = [],
                attributes : list = [],
                move       : int  = 500,
                sound_dict : dict = dict()):
    create_player(name=name,
                  x=x,
                  y=y,
                  frame_id=frame_id,
                  hp=hp,
                  cards=cards,
                  attributes=attributes,
                  move=move,
                  sound_dict=sound_dict)
    push_occupant(x,y,name)
    global _player_list
    global _active_character_id
    _player_list += [name]
    if _active_character_id is None:
        _active_character_id = name
        reroll_cards()

# This function moves a player entity of a given ID to a new position via an
#   x and y difference value (e.g., spaces moved, not new position). The function
#   is just a wrapper for the entity move that checks if the entity is a player.
def move_player(id : str, x_diff : int, y_diff : int, t : int):
    return  is_player(id=id) and \
            entity_move(id=id,
                        x_diff=x_diff,
                        y_diff=y_diff,
                        t=t)

# This function performs an attack of a certain attack index of a player of a 
#   given ID, at the given time t. The function is just a wrapper for the entity 
#   move that checks if the entity is a player.
def player_attack(id : str, attack_idx : int, t : int):
    return  is_player(id=id) and \
            entity_attack(  id=id,
                            attack_idx=attack_idx,
                            t=t)

# True if the given ID is a player (i.e., it is in the player list)
def is_player(id : str):
    return id in _player_list

# True if the given ID is the current active player.
def is_active_player(id : str):
    return id == _active_character_id

# Selects three "cards" from the active player's "deck". The "cards" are the valid
#   attacks the active player may make, and the "deck" is the list of player attacks.
def reroll_cards():
    global _active_cards
    _active_cards = random.sample(range(len(get_char_attacks(_active_character_id))), 3)

# Gets names of the attacks for each of the active cards. Used for graphics.
def get_active_cards():
    return [get_attack_name(get_char_attacks(_active_character_id)[_active_cards[idx]]) for idx in range(len(_active_cards))]

# Performs a command. A player may attempt do any of the following:
#   - Attempt to move (w,a,s,d)
#   - Attempt to attack with one of their cards (q,e,r)
#   - Switch to another player (1,2,3)
# There are no special limitations to how a player moves.
# A player has three cards at a time, drawn from their "deck" of attacks.
#   Only these attacks are valid to be cast.
# A player can only be switched into if they are alive. Switching can
#   only occur from one character to another (i.e., not from one character to themselves),
#   causes a card reroll, and moves the attack timer back to current + 1.5s, unless the attack
#   timer is already greater than that.
def get_command(command : str, t : int):
    global _active_character_id
    match command.lower():
        case 'w':
            move_player(_active_character_id,0,-1,t)
        case 'a':
            move_player(_active_character_id,-1,0,t)
        case 's':
            move_player(_active_character_id,0,1,t)
        case 'd':
            move_player(_active_character_id,1,0,t)
        case 'q':
            if player_attack(_active_character_id, _active_cards[0], t):
                reroll_cards()
        case 'e':
            if player_attack(_active_character_id, _active_cards[1], t):
                reroll_cards()
        case 'r':
            if player_attack(_active_character_id, _active_cards[2], t):
                reroll_cards()
        case '1':
            if  len(_player_list) >= 1 and \
                get_health(_player_list[0]) > 0 and \
                _active_character_id != _player_list[0]:
                    if get_attack_time(_active_character_id) < t+1500:
                        update_attack_time(_active_character_id, t+1500)
                    _active_character_id = _player_list[0]
                    reroll_cards()
        case '2':
            if  len(_player_list) >= 2 and \
                get_health(_player_list[1]) > 0 and \
                _active_character_id != _player_list[1]:
                    if get_attack_time(_active_character_id) < t+1500:
                        update_attack_time(_active_character_id, t+1500)
                    _active_character_id = _player_list[1]
                    reroll_cards()
        case '3':
            if  len(_player_list) >= 3 and \
                get_health(_player_list[2]) > 0 and \
                _active_character_id != _player_list[2]:
                    if get_attack_time(_active_character_id) < t+1500:
                        update_attack_time(_active_character_id, t+1500)
                    _active_character_id = _player_list[2]
                    reroll_cards()

# This function checks if the active player is still alive, and updates the active
#   player to a new player if not. If no player with health above zero exists, returns False.
def check_active_alive():
    global _active_character_id
    if get_health(_active_character_id) > 0:
        return True
    for id in _player_list:
        if get_health(id) > 0:
            _active_character_id = id
            return True
    return False
