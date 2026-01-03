from entity import *
from grid import *

# This function moves an entity of a given ID to a new position via an
#   x and y difference value (e.g., spaces moved, not new position).
def entity_move(id : str, x_diff : int, y_diff : int, t : int):
    if not move_time_valid(id, t):
        return False
    x_old, y_old = get_char_pos(id)
    x = x_old + x_diff
    y = y_old + y_diff
    if not is_empty(x,y):
        return False
    push_occupant(x,y,pop_occupant(x_old,y_old))
    update_position(id,x,y)
    update_move_time(id,t)
    cast_attack(get_entity_footstep_random(id), id, x, y, t)
    return True

# This function performs an attack of a certain attack index of an entity of a 
#   given ID, at the given time t.
def entity_attack(id : str, attack_idx : int, t : int):
    if not attack_time_valid(id, t):
        return False
    x, y = get_char_pos(id)
    attack = get_char_attacks(id)[attack_idx]
    cast_attack(attack, id, x, y, t)
    update_attack_time(id, t+get_cooldown(attack))
    return True


# This function checks for any active attacks that may damage a character at the given
#   x,y coordinates at time t, and performs those damage checks if any exist.
def check_entity_damage(id : str, x : int, y : int, t : int):
    attacks = get_active_attacks(x,y,t)
    for attack in [attack for attack in attacks if not attack[ATTACK_GRID_ENTRY_STARTED] and attack[ATTACK_GRID_ENTRY_CASTER] != id]:
        damage_entity(id, attack[ATTACK_GRID_ENTRY_DAMAGE])
        attack[ATTACK_GRID_ENTRY_STARTED] = True

# This function checks all grid tiles for any damage that needs to be handled, handles them
#   if the entity has positive health, then removes any entities from the grid (but not the
#   entity list) if they fall below 0 HP.
def check_entity_damage_all(t : int):
    for x in range(GRID_X_DIM):
        for y in range(GRID_Y_DIM):
            id = get_occupant(x,y)
            if id is None:
                continue
            if get_health(id) > 0:
                check_entity_damage(id,x,y,t)
            if get_health(id) <= 0:
                pop_occupant(x,y)