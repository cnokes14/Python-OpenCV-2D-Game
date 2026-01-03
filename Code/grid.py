from attack import *

# The grid is a 10*4 board, though initialized as a simple 1D array.
#   Each grid entry contains the following:
#       occupant---the id of whatever entity currently occupies the grid, or None
#       attacks----list of all current attack grid entries
#       effects----unused
_GRID_X = 10
_GRID_Y = 4

GRID_X_DIM = _GRID_X
GRID_Y_DIM = _GRID_Y

_GRID_TILE_OCCUPANT = "occupant"
_GRID_TILE_ATTACKS  = "attacks"
_GRID_TILE_EFFECTS  = "effects"

_EMPTY_GRID_TILE = {
    _GRID_TILE_OCCUPANT : None,
    _GRID_TILE_ATTACKS : [],
    _GRID_TILE_EFFECTS : []
}

_grid = [_EMPTY_GRID_TILE.copy() for _ in range(_GRID_X*_GRID_Y)]

# Checks if a given x y position exists on the board
def is_valid(x : int, y : int):
    return not (x < 0 or x >= _GRID_X or y < 0 or y >= _GRID_Y)

# Gets the grid dict at a given x y position.
def _get_grid(x : int, y : int):
    if not is_valid(x=x,y=y):
        return None
    return _grid[x + y*_GRID_X]

# Adds a list of attack grid entries to the grid entry at a given x y position
def _add_attacks(attacks : list[dict], x : int, y : int):
    entry = _get_grid(x, y)
    if (entry is None):
        return False
    entry[_GRID_TILE_ATTACKS] += attacks
    return True

# True if an x y space exists and is occupied, False otherwise.
def has_occupants(x : int, y : int):
    entry = _get_grid(x=x,y=y)
    return entry is not None and entry[_GRID_TILE_OCCUPANT] != None

# True if an x y space exists and is not occupied, False otherwise.
def is_empty(x : int, y : int):
    entry = _get_grid(x=x,y=y)
    return entry is not None and entry[_GRID_TILE_OCCUPANT] == None

# Gets the ID of the entity occupying a given x y position, or None.
def get_occupant(x : int, y : int):
    entry = _get_grid(x, y)
    if (entry is None):
        return None
    return entry[_GRID_TILE_OCCUPANT]

# Gets the occupant of an x y position (or None) and replaces it with None.
def pop_occupant(x : int, y : int):
    entry = _get_grid(x, y)
    if (entry is None):
        return None
    occupant = entry[_GRID_TILE_OCCUPANT]
    entry[_GRID_TILE_OCCUPANT] = None
    return occupant

# Puts an entity at an x y position on the board, if it is valid, even if occupied.
def push_occupant(x : int, y : int, id : str):
    entry = _get_grid(x, y)
    if (entry is None):
        return False
    entry[_GRID_TILE_OCCUPANT] = id
    return True

# Gets all active attack grid entries on the board.
def get_active_attacks(x : int, y : int, t : int):
    entry = _get_grid(x, y)
    if (entry is None):
        return []
    return [attack for attack in entry[_GRID_TILE_ATTACKS] \
            if  attack[ATTACK_GRID_ENTRY_START] <= t and \
                attack[ATTACK_GRID_ENTRY_END] > t]

# Removes all attacks on an x y grid space that ended before current time t.
def _prune_expired_attacks(x : int, y : int, t : int):
    entry = _get_grid(x, y)
    if (entry is None):
        return False
    entry[_GRID_TILE_ATTACKS] = [attack for attack in entry[_GRID_TILE_ATTACKS] \
                                    if attack[ATTACK_GRID_ENTRY_END] > t]
    return True

# Deploys an attack given a caster id and x y position, and the current time.
#   Converts the attack to a set of attack grid entries at each space on the grid,
#   and adds those to the grid spaces.
def cast_attack(attack : dict, 
                caster_id : str,
                caster_x : int,
                caster_y : int,
                t : int):
    if attack is None:
        return False
    for x in range(_GRID_X):
        for y in range(_GRID_Y):
            entries = attack_at_pos_to_grid_entries(attack=attack, t=t, caster_id=caster_id,
                                                    caster_x=caster_x, caster_y=caster_y,
                                                    pos_x=x, pos_y=y)
            _add_attacks(entries, x, y)
    return True

# Removes all attacks that ended before current time t.
def prune_expired_attacks_all(t : int):
    for x in range(_GRID_X):
        for y in range(_GRID_Y):
            _prune_expired_attacks(x,y,t)