from id_list import *
from grid import *
from playsound3 import *
from common_util import *

# All sound effects were taken from https://pixabay.com/, with some slight editing done
#   via Audacity. Music was made by a friend and has been uploaded with approval.
_PISTOL_FIRE            = get_fpath() + "\\Sounds\\Weapon\\pistol_0.mp3"
_RIFLE_FIRE             = get_fpath() + "\\Sounds\\Weapon\\rifle_0.mp3"
_HAWK_SLASH_0           = get_fpath() + "\\Sounds\\Weapon\\hawk_slash_0.mp3"
_HAWK_SLASH_1           = get_fpath() + "\\Sounds\\Weapon\\hawk_slash_1.mp3"
_HAWK_SLASH_2           = get_fpath() + "\\Sounds\\Weapon\\hawk_slash_2.mp3"
_HAWK_DRAW              = get_fpath() + "\\Sounds\\Weapon\\hawk_draw.mp3"
_GUARDSMAN_FOOTSTEP_0   = get_fpath() + "\\Sounds\\Footsteps\\footstep_guardsman.mp3"
_GUARDSMAN_FOOTSTEP_1   = get_fpath() + "\\Sounds\\Footsteps\\footstep_guardsman_2.mp3"
_TRAIN_BACKGROUND       = get_fpath() + "\\Sounds\\Background\\train.mp3"
_KALKUTTA_COMBAT_OST    = get_fpath() + "\\Sounds\\Music\\kalkutta_combat.mp3"

_sound_map = {
    TAG_PISTOL_FIRE             : _PISTOL_FIRE,
    TAG_RIFLE_FIRE              : _RIFLE_FIRE,
    TAG_GUARDSMAN_FOOTSTEP_0    : _GUARDSMAN_FOOTSTEP_0,
    TAG_GUARDSMAN_FOOTSTEP_1    : _GUARDSMAN_FOOTSTEP_1,
    TAG_HAWK_SLASH_0            : _HAWK_SLASH_0,
    TAG_HAWK_SLASH_1            : _HAWK_SLASH_1,
    TAG_HAWK_SLASH_2            : _HAWK_SLASH_2,
    TAG_HAWK_DRAW               : _HAWK_DRAW,
    TAG_TRAIN_BACKGROUND        : _TRAIN_BACKGROUND,
    TAG_KALKUTTA_COMBAT_OST     : _KALKUTTA_COMBAT_OST,
}

# Plays the sounds for all attacks that are active, but have not yet sounded.
#   It is expected that actions that need sounds but aren't attacks are still triggered
#   as attacks to allow them to play.
def play_soundset(lst : list):
    if lst is None or lst == []:
        return False
    for entry in lst:
        entry_sound = entry[ATTACK_GRID_ENTRY_SOUND]
        if entry[ATTACK_GRID_ENTRY_SOUND_STARTED] or entry_sound not in _sound_map:
            continue
        playsound(_sound_map[entry_sound],block=False)
        entry[ATTACK_GRID_ENTRY_SOUND_STARTED] = True

# What sounds are tied to the map, rather than entities or attacks?
_background_sounds = []

# Starts a list of background sounds.
def init_background_sounds(lst : list):
    global _background_sounds
    for entry in lst:
        _background_sounds += [[entry,playsound(_sound_map[entry], block=False)]]

# Checks all background sounds and plays any that have stopped.
def check_background_sounds():
    global _background_sounds
    for sound in [sound for sound in _background_sounds if not sound[1].is_alive()]:
        sound[1] = playsound(_sound_map[sound[0]], block=False)

# When did we last check in with the global sound list?
_last_global_soundcheck = 0

# Starts playing all new sounds. Additionally, sometimes checks in with background sounds
#   to ensure that all of them are still playing as expected.
# Sounds are played in the same order that images are rendered, though this should
#   make little difference.
def start_sounds(t : int):
    global _last_global_soundcheck
    if t - _last_global_soundcheck > 3000:
        check_background_sounds()
        _last_global_soundcheck = t
    for y in range(GRID_Y_DIM):
        for x in range(GRID_X_DIM):
            play_soundset(get_active_attacks(x,y,t))