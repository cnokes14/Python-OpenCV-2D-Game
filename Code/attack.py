# An attack "frame" is an individual damage instance on an
#   individual tile. It has warning and damaging components,
#   where a warn image and warn sound, and damage image and
#   damage sound, respectively, are shown.
# An attack frame has components:
#   Warn time-----time after cast time that the warning displays
#   Damage time---time after warn time that damage begins
#   End time------time after damage that the attack frame ends
#   Damage--------damage dealt by the frame
#   x offset------x offset from the caster
#   y offset------y offset from the caster
#   warn image----tag of image set displayed during the warning phase
#   damage image--tag of image set  displayed during the damage phase
#   warn sound----tag of sound played at the start of the warning phase
#   damage sound--tag of sound played at the start of the damage phase
_ATTACK_FRAME_WARN_TIME_TAG     = "warn_t"
_ATTACK_FRAME_DAMAGE_TIME_TAG   = "damage_t"
_ATTACK_FRAME_END_TIME_TAG      = "end_t"
_ATTACK_FRAME_DAMAGE_TAG        = "damage"
_ATTACK_FRAME_X_DIFF_TAG        = "x"
_ATTACK_FRAME_Y_DIFF_TAG        = "y"
_ATTACK_FRAME_WARN_IMG_TAG      = "warn_img"
_ATTACK_FRAME_DAMAGE_IMG_TAG    = "damage_img"
_ATTACK_FRAME_WARN_SOUND        = "warn_sound"
_ATTACK_FRAME_DAMAGE_SOUND      = "damage_sound"

_EMPTY_ATTACK_FRAME = {
    _ATTACK_FRAME_WARN_TIME_TAG     : -1,
    _ATTACK_FRAME_DAMAGE_TIME_TAG   : -1,
    _ATTACK_FRAME_END_TIME_TAG      : -1,
    _ATTACK_FRAME_DAMAGE_TAG        : 0,
    _ATTACK_FRAME_X_DIFF_TAG        : -999,
    _ATTACK_FRAME_Y_DIFF_TAG        : -999,
    _ATTACK_FRAME_WARN_IMG_TAG      : "PH",
    _ATTACK_FRAME_DAMAGE_IMG_TAG    : "PH",
    _ATTACK_FRAME_WARN_SOUND        : "PH",
    _ATTACK_FRAME_DAMAGE_SOUND      : "PH",
}


# An attack consists of:
#   Name------attack identifier. Not required to be unique; used for UI on player attacks
#   Frames----list of all attack frames.
#   Cooldown--time after this attack is used, until another attack can be used.
#               No restraint on this value, but value is normally in [0,5000]
_ATTACK_NAME                    = "name"
_ATTACK_LIST_FRAMES_TAG         = "frames"
_ATTACK_COOLDOWN_TIME_TAG       = "cooldown"

_EMPTY_ATTACK = {
    _ATTACK_NAME                : "PH",
    _ATTACK_LIST_FRAMES_TAG     : [],
    _ATTACK_COOLDOWN_TIME_TAG   : -1
}

# An attack grid entry is constructed for each grid space effected by an attack cast.
#   These are public, and are used to calculate damage to targets and display graphics.
#   As such, this attack structure is opaque to anyone with knowledge of attacks.
# An attack grid entry consists of:
#   Damage--------damage dealt
#   Start---------time the attack starts
#   End-----------time the attack ends
#   Sound---------tag of the sound played on attack start
#   Image---------tag of the image set displayed while the attack is active.
#   Caster--------who caused this attack? Used to prevent self-damage.
#   Started-------has the attack started? Used to prevent duplicate damage.
#   Sounded-------has the attack sound been triggered? Used to prevent duplicate plays.
ATTACK_GRID_ENTRY_DAMAGE       = "damage"
ATTACK_GRID_ENTRY_START        = "start_t"
ATTACK_GRID_ENTRY_END          = "end_t"
ATTACK_GRID_ENTRY_SOUND        = "sound"
ATTACK_GRID_ENTRY_IMAGE        = "img"
ATTACK_GRID_ENTRY_CASTER       = "caster"
ATTACK_GRID_ENTRY_STARTED      = "started"
ATTACK_GRID_ENTRY_SOUND_STARTED= "sound_started"

_EMPTY_ATTACK_GRID_ENTRY = {
    ATTACK_GRID_ENTRY_DAMAGE            : 0,
    ATTACK_GRID_ENTRY_START             : -1,
    ATTACK_GRID_ENTRY_END               : -1,
    ATTACK_GRID_ENTRY_SOUND             : "PH",
    ATTACK_GRID_ENTRY_IMAGE             : "PH",
    ATTACK_GRID_ENTRY_CASTER            : "PH",
    ATTACK_GRID_ENTRY_STARTED           : False,
    ATTACK_GRID_ENTRY_SOUND_STARTED     : False
}

# This local function takes an individual frame and builds a "warning" from it.
#   A warning is an attack that deals no damage. When constructed normally,
#   it occurs before the damage section of an attack, until the damage section starts.
# The function has the following inputs:
#   attack_frame---attack frame from which the attack is derived
#   caster---------string ID of the attack caster
#   t--------------time of cast, in ms
# The function returns the following:
#   warning--------constructed warning attack grid entry
def _create_warning(attack_frame : dict, caster : str, t : int):
    warning = _EMPTY_ATTACK_GRID_ENTRY.copy()
    warning[ATTACK_GRID_ENTRY_DAMAGE]   = 0
    warning[ATTACK_GRID_ENTRY_START]    = t + attack_frame[_ATTACK_FRAME_WARN_TIME_TAG]
    warning[ATTACK_GRID_ENTRY_END]      = t + attack_frame[_ATTACK_FRAME_WARN_TIME_TAG] + \
                                              attack_frame[_ATTACK_FRAME_DAMAGE_TIME_TAG]
    warning[ATTACK_GRID_ENTRY_SOUND]    = attack_frame[_ATTACK_FRAME_WARN_SOUND]
    warning[ATTACK_GRID_ENTRY_IMAGE]    = attack_frame[_ATTACK_FRAME_WARN_IMG_TAG]
    warning[ATTACK_GRID_ENTRY_CASTER]   = caster
    warning[ATTACK_GRID_ENTRY_STARTED]  = False
    warning[ATTACK_GRID_ENTRY_SOUND_STARTED]  = False
    return warning

# This local function takes an individual frame and builds the "damaging" stage.
#   The damaging stage occurs after the warning stage, if a warning stage exists.
#   It can deal damage, though it does not necessarily have to.
# The function has the following inputs:
#   attack_frame---attack frame from which the attack is derived
#   caster---------string ID of the attack caster
#   t--------------time of cast, in ms
# The function returns the following:
#   damaging--------constructed damaging attack grid entry
def _create_damaging(attack_frame : dict, caster : str, t : int):
    damaging = _EMPTY_ATTACK_GRID_ENTRY.copy()
    damaging[ATTACK_GRID_ENTRY_DAMAGE]   = attack_frame[_ATTACK_FRAME_DAMAGE_TAG]
    damaging[ATTACK_GRID_ENTRY_START]    = t + attack_frame[_ATTACK_FRAME_WARN_TIME_TAG] + \
                                               attack_frame[_ATTACK_FRAME_DAMAGE_TIME_TAG]
    damaging[ATTACK_GRID_ENTRY_END]      = t + attack_frame[_ATTACK_FRAME_WARN_TIME_TAG] + \
                                               attack_frame[_ATTACK_FRAME_DAMAGE_TIME_TAG] + \
                                               attack_frame[_ATTACK_FRAME_END_TIME_TAG]
    damaging[ATTACK_GRID_ENTRY_SOUND]    = attack_frame[_ATTACK_FRAME_DAMAGE_SOUND]
    damaging[ATTACK_GRID_ENTRY_IMAGE]    = attack_frame[_ATTACK_FRAME_DAMAGE_IMG_TAG]
    damaging[ATTACK_GRID_ENTRY_CASTER]   = caster
    damaging[ATTACK_GRID_ENTRY_STARTED]  = False
    damaging[ATTACK_GRID_ENTRY_SOUND_STARTED]  = False
    return damaging

# This local function converts an individual attack frame into attack grid entries.
#   Currently, only a damaging and warning stage are constructed; the damaging stage
#   is always constructed, but the warning stage is only constructed if the warning
#   time is non-zero.
# The function has inputs:
#   attack_frame---attack frame from which the attack is derived
#   caster---------string ID of the attack caster
#   t--------------time of cast, in ms
# The function returns:
#   entries--------array of constructed attack grid entries.
def _attack_frame_to_grid_entries(attack_frame : dict, caster : str, t : int):
    entries = []
    if attack_frame[_ATTACK_FRAME_DAMAGE_TIME_TAG] > 0:
        entries += [_create_warning(attack_frame, caster, t)]
    entries += [_create_damaging(attack_frame, caster, t)]
    return entries

# This function takes a target x,y coordinate pair and an attack with a caster,
#   and builds all attack grid entries for the attack that will occur at that point.
# The function has inputs:
#   attack----------full attack. While other files will not understand the attack,
#                       since they can only access the grid entries, they can still
#                       pass around the full attack before casting.
#   t---------------time of cast
#   caster_id-------string ID of the attack caster
#   caster_x--------x coordinate of the caster
#   caster_y--------y coordinate of the caster
#   pos_x-----------x coordinate to check
#   pos_y-----------y coordinate to check
# This function returns:
#   entries---------list of all attack grid entries at the given x,y point.
def attack_at_pos_to_grid_entries(attack : dict,
                                  t : int,
                                  caster_id: str,
                                  caster_x : int,
                                  caster_y : int,
                                  pos_x : int,
                                  pos_y : int):
    result = []
    for entry in attack[_ATTACK_LIST_FRAMES_TAG]:
        if  entry[_ATTACK_FRAME_X_DIFF_TAG] + caster_x == pos_x and \
            entry[_ATTACK_FRAME_Y_DIFF_TAG] + caster_y == pos_y:
                result += _attack_frame_to_grid_entries(entry, caster_id, t)
    return result

# This function creates an individual attack frame. Currently, there is no
#   advanced calculation done here, it just copies the blank attack frame
#   and fills it out based on the input. The function is largely used for code neatening.
# This function takes inputs:
#   warn_t--------time after cast time that the warning displays
#   damage_t------time after warn time that damage begins
#   end_t---------time after damage that the attack frame ends
#   damage--------damage dealt by the frame
#   x_diff--------x offset from the caster
#   y_diff--------y offset from the caster
#   warn_img------tag of image set displayed during the warning phase
#   damage_img----tag of image set displayed during the damage phase
#   warn_sound----tag of sound played at the start of the warning phase
#   damage_sound--tag of sound played at the start of the damage phase
# This function returns:
#   frame---------constructed attack frame
def create_attack_frame(warn_t          : int,
                        damage_t        : int,
                        end_t           : int,
                        damage          : int,
                        x_diff          : int,
                        y_diff          : int,
                        warn_img        : str = "PH",
                        damage_img      : str = "PH",
                        warn_sound      : str = "PH",
                        damage_sound    : str = "PH"):
    frame = _EMPTY_ATTACK_FRAME.copy()
    frame[_ATTACK_FRAME_WARN_TIME_TAG]  = warn_t
    frame[_ATTACK_FRAME_DAMAGE_TIME_TAG]= damage_t
    frame[_ATTACK_FRAME_END_TIME_TAG]   = end_t
    frame[_ATTACK_FRAME_DAMAGE_TAG]     = damage
    frame[_ATTACK_FRAME_X_DIFF_TAG]     = x_diff
    frame[_ATTACK_FRAME_Y_DIFF_TAG]     = y_diff
    frame[_ATTACK_FRAME_WARN_IMG_TAG]   = warn_img
    frame[_ATTACK_FRAME_DAMAGE_IMG_TAG] = damage_img
    frame[_ATTACK_FRAME_WARN_SOUND]     = warn_sound
    frame[_ATTACK_FRAME_DAMAGE_SOUND]   = damage_sound
    return frame

# This function creates an full attack. Currently, there is no advanced calculation done here, it just copies
#   the blank attack frame and fills it out based on the input. The function is largely used for code neatening.
# This function has inputs:
#   name--------name of the attack, does not need to be unique
#   frames------list of attack frames
#   cooldown----time until the attacker may attack again after performing this
# This function returns:
#   attack------constructed attack
def create_attack(name : str, frames : list[dict], cooldown : int):
    attack = _EMPTY_ATTACK.copy()
    attack[_ATTACK_NAME]                = name
    attack[_ATTACK_LIST_FRAMES_TAG]     = frames
    attack[_ATTACK_COOLDOWN_TIME_TAG]   = cooldown
    return attack

# This function retrieves the cooldown from an attack dict.
# This function has inputs:
#   attack-----given attack dict
# This function returns:
#   cooldown---cooldown time
def get_cooldown(attack : dict):
    return attack[_ATTACK_COOLDOWN_TIME_TAG]

# This function retrieves the name from an attack dict.
# This function has inputs:
#   attack-----given attack dict
# This function returns:
#   name-------attack name
def get_attack_name(attack : dict):
    return attack[_ATTACK_NAME]

# This function takes an attack and caster, and determines when the first attack
#   at a given set of coordinates will occur. 
# This function has inputs:
#   attack-------attack to trace
#   caster_x-----attack caster x coordinate
#   caster_y-----attack caster y coordinate
#   pos_x--------target x coordinate
#   pos_y--------target y coordinate
# This function returns:
#   min_time-----time, in ms, from current when the next attack at the target point occurs
def soonest_hit(attack : dict,
                caster_x : int,
                caster_y : int,
                pos_x : int, 
                pos_y : int):
    result = -1
    for entry in attack[_ATTACK_LIST_FRAMES_TAG]:
        hit_time = entry[_ATTACK_FRAME_WARN_TIME_TAG] + entry[_ATTACK_FRAME_DAMAGE_TIME_TAG]
        if  entry[_ATTACK_FRAME_X_DIFF_TAG] + caster_x == pos_x and \
            entry[_ATTACK_FRAME_Y_DIFF_TAG] + caster_y == pos_y and \
            (hit_time < result or result == -1):
                result = hit_time
    return result