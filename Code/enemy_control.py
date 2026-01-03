from entity_control import *
from player_control import *

# This maintains a list of all enemies, including those that are dead.
_enemy_list = []

# This function creates an enemy entity, pushes it to the grid, and adds it
#   to the list of enemies.
def add_enemy(  name       : str, 
                x          : int, 
                y          : int,
                frame_id   : str,
                hp         : int  = 1,
                attacks      : list = [],
                attributes : list = [],
                move_min   : int  = 500,
                move_max   : int  = 500,
                sound_dict : dict = dict()):
    create_enemy(name=name,
                  x=x,
                  y=y,
                  frame_id=frame_id,
                  hp=hp,
                  attacks=attacks,
                  attributes=attributes,
                  move_min=move_min,
                  move_max=move_max,
                  sound_dict=sound_dict)
    push_occupant(x,y,name)
    global _enemy_list
    _enemy_list += [name]

# This function moves an enemy entity of a given ID to a new position via an
#   x and y difference value (e.g., spaces moved, not new position). The function
#   is just a wrapper for the entity move that checks if the entity is an enemy.
def enemy_move(id : str, x_diff : int, y_diff : int, t : int):
    return  is_enemy(id=id) and \
            entity_move(id=id,
                        x_diff=x_diff,
                        y_diff=y_diff,
                        t=t)

# This function performs an attack of a certain attack index of an enemy of a 
#   given ID, at the given time t. The function is just a wrapper for the entity 
#   move that checks if the entity is an enemy.
def enemy_attack(id : str, attack_idx : int, t : int):
    return  is_enemy(id=id) and \
            entity_attack(  id=id,
                            attack_idx=attack_idx,
                            t=t)

# Checks if an entity is in the enemy list.
def is_enemy(id : str):
    return id in _enemy_list

# This function gets a list of all active players and their X,Y positions.
#   This function is mostly used for determining enemy actions.
def _get_players():
    players = []
    for x in range(GRID_X_DIM):
        for y in range(GRID_Y_DIM):
            id = get_occupant(x,y)
            if id is not None and is_player(id) and get_health(id) > 0:
                players += [[id, x, y]]
    return players

# This function looks through all players in a given list and, based on a given
#   attack and given attacker position, determines the "quality". Quality is two metrics:
#   (1) when the first player will be hit and (2) how many players are hit.
def _get_attack_data(attack : dict, players : list, caster_x : int, caster_y : int):
    soonest = -1
    count = 0
    for player in players:
        t_hit = soonest_hit(attack, caster_x, caster_y, player[1], player[2])
        if t_hit < soonest or soonest == -1:
            soonest = t_hit
        if t_hit != -1:
            count += 1
    return [soonest, count]

# This function, given the position of a caster, the intended move of the caster, and the
#   list of all active players, determines the distance to the nearest player.
def _dir_to_player(caster_x : int, caster_y : int, diff_x : int, diff_y : int, players : list):
    new_x = caster_x + diff_x
    new_y = caster_y + diff_y
    if (new_x != caster_x or new_y != caster_y) and not is_empty(new_x,new_y):
        return -1
    min_dist = -1
    for player in players:
        a = new_x-player[1]
        b = new_y-player[2]
        dist = a*a + b*b
        if dist < min_dist or min_dist == -1:
            min_dist = dist
    return min_dist

# This function checks the distance between a caster and all players for all possible
#   moves (including no move), and returns the best possible move as an [x,y] pair.
def _get_best_dir(caster_x : int, caster_y : int, players : list):
    best_dist   = _dir_to_player(caster_x,caster_y,0,0,players)
    best_dir    = [0,0]
    for diff in [[-1,0],[1,0],[0,-1],[0,1]]:
        dist = _dir_to_player(caster_x,caster_y,diff[0],diff[1],players)
        if dist != -1 and dist < best_dist:
            best_dir = diff
            best_dist = dist
    return best_dir

# This function performs an action for a given enemy at a given time t. Enemy pathing is simple:
#   1. If we can attack, check to see what the best attack is based on how many players are hit and when.
#   2. If the best attack is good, we make that attack and exit.
#   3. If the best attack is not good, we attempt to move instead, if possible.
#   4. If we can move, move in the direction that gets us closer to a player, if one exists.
# Returns true if an action is taken, or false otherwise.
def take_action(id : str, t : int):
    if not is_enemy(id):
        return False
    can_attack  = attack_time_valid(id, t)
    can_move    = move_time_valid(id, t)
    px, py      = get_char_pos(id)
    players     = _get_players()
    if can_attack:
        attacks     = get_char_attacks(id)
        results     = []
        for attack_idx in range(len(attacks)):
            attack = attacks[attack_idx]
            results += [_get_attack_data(attack, players, px, py)]
        best_idx = -1
        best_value = 0
        for result_idx in range(len(results)):
            result = results[result_idx][1] * (1.0 / results[result_idx][0])
            if result > best_value:
                best_idx = result_idx
                best_value = result
        if best_idx != -1:
            enemy_attack(id, best_idx, t)
            return True
    if can_move:
        dir = _get_best_dir(px,py,players)
        if dir == [0,0]:
            return False
        return enemy_move(id, dir[0], dir[1], t)
    return False

# This function performs updates for all enemies currently alive.
def enemy_actions(t : int):
    for enemy in [enemy for enemy in _enemy_list if get_health(enemy) > 0]:
        take_action(enemy, t)