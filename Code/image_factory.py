import cv2
from id_list import *
from common_util import *

_GMAN_0 = get_fpath() + "\\PNGs\\guardsman_basic\\sprite_0.png"
_GMAN_1 = get_fpath() + "\\PNGs\\guardsman_basic\\sprite_1.png"
_GMAN_2 = get_fpath() + "\\PNGs\\guardsman_basic\\sprite_2.png"
_GMAN_3 = get_fpath() + "\\PNGs\\guardsman_basic\\sprite_3.png"
_GMAN_LST       =   [_GMAN_0,_GMAN_1,_GMAN_2,_GMAN_3]

_VEIL_0 = get_fpath() + "\\PNGs\\veil\\sprite_0.png"
_VEIL_1 = get_fpath() + "\\PNGs\\veil\\sprite_1.png"
_VEIL_2 = get_fpath() + "\\PNGs\\veil\\sprite_2.png"
_VEIL_3 = get_fpath() + "\\PNGs\\veil\\sprite_3.png"
_VEIL_4 = get_fpath() + "\\PNGs\\veil\\sprite_4.png"
_VEIL_5 = get_fpath() + "\\PNGs\\veil\\sprite_5.png"
_VEIL_LST       =   [_VEIL_0,_VEIL_1,_VEIL_2,_VEIL_3,_VEIL_4,_VEIL_5]

_HAWK_0 = get_fpath() + "\\PNGs\\reval_kyetn_hawk\\sprite_0.png"
_HAWK_1 = get_fpath() + "\\PNGs\\reval_kyetn_hawk\\sprite_1.png"
_HAWK_2 = get_fpath() + "\\PNGs\\reval_kyetn_hawk\\sprite_2.png"
_HAWK_LST       =   [_HAWK_0,_HAWK_1,_HAWK_2]

_STAMINA_0 = get_fpath() + "\\PNGs\\stamina\\sprite_00.png"
_STAMINA_1 = get_fpath() + "\\PNGs\\stamina\\sprite_01.png"
_STAMINA_2 = get_fpath() + "\\PNGs\\stamina\\sprite_02.png"
_STAMINA_3 = get_fpath() + "\\PNGs\\stamina\\sprite_03.png"
_STAMINA_4 = get_fpath() + "\\PNGs\\stamina\\sprite_04.png"
_STAMINA_5 = get_fpath() + "\\PNGs\\stamina\\sprite_05.png"
_STAMINA_6 = get_fpath() + "\\PNGs\\stamina\\sprite_06.png"
_STAMINA_7 = get_fpath() + "\\PNGs\\stamina\\sprite_07.png"
_STAMINA_8 = get_fpath() + "\\PNGs\\stamina\\sprite_08.png"
_STAMINA_9 = get_fpath() + "\\PNGs\\stamina\\sprite_09.png"
_STAMINA_10 = get_fpath() + "\\PNGs\\stamina\\sprite_10.png"
_STAMINA_11 = get_fpath() + "\\PNGs\\stamina\\sprite_11.png"
_STAMINA_12 = get_fpath() + "\\PNGs\\stamina\\sprite_12.png"
_STAMINA_13 = get_fpath() + "\\PNGs\\stamina\\sprite_13.png"
_STAMINA_LST       =   [_STAMINA_13,_STAMINA_12,_STAMINA_11,_STAMINA_10,_STAMINA_9,_STAMINA_8,_STAMINA_7,_STAMINA_6,
                       _STAMINA_5,_STAMINA_4,_STAMINA_3,_STAMINA_2,_STAMINA_1,_STAMINA_0]

_HEALTH_0 = get_fpath() + "\\PNGs\\health\\sprite_00.png"
_HEALTH_1 = get_fpath() + "\\PNGs\\health\\sprite_01.png"
_HEALTH_2 = get_fpath() + "\\PNGs\\health\\sprite_02.png"
_HEALTH_3 = get_fpath() + "\\PNGs\\health\\sprite_03.png"
_HEALTH_4 = get_fpath() + "\\PNGs\\health\\sprite_04.png"
_HEALTH_5 = get_fpath() + "\\PNGs\\health\\sprite_05.png"
_HEALTH_6 = get_fpath() + "\\PNGs\\health\\sprite_06.png"
_HEALTH_7 = get_fpath() + "\\PNGs\\health\\sprite_07.png"
_HEALTH_8 = get_fpath() + "\\PNGs\\health\\sprite_08.png"
_HEALTH_9 = get_fpath() + "\\PNGs\\health\\sprite_09.png"
_HEALTH_10 = get_fpath() + "\\PNGs\\health\\sprite_10.png"
_HEALTH_11 = get_fpath() + "\\PNGs\\health\\sprite_11.png"
_HEALTH_12 = get_fpath() + "\\PNGs\\health\\sprite_12.png"
_HEALTH_13 = get_fpath() + "\\PNGs\\health\\sprite_13.png"
_HEALTH_LST       =   [_HEALTH_0,_HEALTH_1,_HEALTH_2,_HEALTH_3,_HEALTH_4,_HEALTH_5,_HEALTH_6,_HEALTH_7,
                       _HEALTH_8,_HEALTH_9,_HEALTH_10,_HEALTH_11,_HEALTH_12,_HEALTH_13]

_ENEMY_HP_0 = get_fpath() + "\\PNGs\\health_enemy\\sprite_00.png"
_ENEMY_HP_1 = get_fpath() + "\\PNGs\\health_enemy\\sprite_01.png"
_ENEMY_HP_2 = get_fpath() + "\\PNGs\\health_enemy\\sprite_02.png"
_ENEMY_HP_3 = get_fpath() + "\\PNGs\\health_enemy\\sprite_03.png"
_ENEMY_HP_4 = get_fpath() + "\\PNGs\\health_enemy\\sprite_04.png"
_ENEMY_HP_5 = get_fpath() + "\\PNGs\\health_enemy\\sprite_05.png"
_ENEMY_HP_6 = get_fpath() + "\\PNGs\\health_enemy\\sprite_06.png"
_ENEMY_HP_7 = get_fpath() + "\\PNGs\\health_enemy\\sprite_07.png"
_ENEMY_HP_8 = get_fpath() + "\\PNGs\\health_enemy\\sprite_08.png"
_ENEMY_HP_9 = get_fpath() + "\\PNGs\\health_enemy\\sprite_09.png"
_ENEMY_HP_10 = get_fpath() + "\\PNGs\\health_enemy\\sprite_10.png"
_ENEMY_HP_11 = get_fpath() + "\\PNGs\\health_enemy\\sprite_11.png"
_ENEMY_HP_12 = get_fpath() + "\\PNGs\\health_enemy\\sprite_12.png"
_ENEMY_HP_LST   =   [_ENEMY_HP_0,_ENEMY_HP_1,_ENEMY_HP_2,_ENEMY_HP_3,_ENEMY_HP_4,_ENEMY_HP_5,_ENEMY_HP_6,
                       _ENEMY_HP_7,_ENEMY_HP_8,_ENEMY_HP_9,_ENEMY_HP_10,_ENEMY_HP_11,_ENEMY_HP_12]

_TMP_BACK_0 = get_fpath() + "\\PNGs\\background_train_larger\\sprite_0.png"
_TMP_BACK_1 = get_fpath() + "\\PNGs\\background_train_larger\\sprite_1.png"
_TMP_BACK_2 = get_fpath() + "\\PNGs\\background_train_larger\\sprite_2.png"
_TMP_BACK_3 = get_fpath() + "\\PNGs\\background_train_larger\\sprite_3.png"
_TMP_BACK_4 = get_fpath() + "\\PNGs\\background_train_larger\\sprite_4.png"
_TMP_BACK_5 = get_fpath() + "\\PNGs\\background_train_larger\\sprite_5.png"
_TMP_BACK_LST = [_TMP_BACK_0,_TMP_BACK_1,_TMP_BACK_2,_TMP_BACK_3,_TMP_BACK_4,_TMP_BACK_5]

_TMP_WARN_0 = get_fpath() + "\\PNGs\\tmp\\warn.png"
_TMP_WARN_LST = [_TMP_WARN_0]

_TMP_DMG_0 = get_fpath() + "\\PNGs\\tmp\\damage.png"
_TMP_DMG_LST = [_TMP_DMG_0]

_TMP_ACTIVE_0 = get_fpath() + "\\PNGs\\tmp\\active.png"
_TMP_ACTIVE_LST = [_TMP_ACTIVE_0]

_PISTOL_LEFT_0 = get_fpath() + "\\PNGs\\cards\\sprite_00.png"
_PISTOL_LEFT_1 = get_fpath() + "\\PNGs\\cards\\sprite_01.png"
_PISTOL_LEFT_2 = get_fpath() + "\\PNGs\\cards\\sprite_02.png"
_PISTOL_LEFT_LST = [_PISTOL_LEFT_0,_PISTOL_LEFT_1,_PISTOL_LEFT_2]

_PISTOL_RIGHT_0 = get_fpath() + "\\PNGs\\cards\\sprite_03.png"
_PISTOL_RIGHT_1 = get_fpath() + "\\PNGs\\cards\\sprite_04.png"
_PISTOL_RIGHT_2 = get_fpath() + "\\PNGs\\cards\\sprite_05.png"
_PISTOL_RIGHT_LST = [_PISTOL_RIGHT_0,_PISTOL_RIGHT_1,_PISTOL_RIGHT_2]

_PISTOL_DOWN_0 = get_fpath() + "\\PNGs\\cards\\sprite_06.png"
_PISTOL_DOWN_1 = get_fpath() + "\\PNGs\\cards\\sprite_07.png"
_PISTOL_DOWN_2 = get_fpath() + "\\PNGs\\cards\\sprite_08.png"
_PISTOL_DOWN_LST = [_PISTOL_DOWN_0,_PISTOL_DOWN_1,_PISTOL_DOWN_2]

_PISTOL_UP_0 = get_fpath() + "\\PNGs\\cards\\sprite_09.png"
_PISTOL_UP_1 = get_fpath() + "\\PNGs\\cards\\sprite_10.png"
_PISTOL_UP_2 = get_fpath() + "\\PNGs\\cards\\sprite_11.png"
_PISTOL_UP_LST = [_PISTOL_UP_0,_PISTOL_UP_1,_PISTOL_UP_2]

_NO_CARDS_0 = get_fpath() + "\\PNGs\\cards\\sprite_12.png"
_NO_CARDS_LST = [_NO_CARDS_0]

# A frame dict is a dictionary of frames for a certain entity, object, or other thing.
#   A frame dict should have components:
#       loaded---are the images loaded into memory?
#       data-----the actual image data
#       files----file locations of the frames
#       fcount---len(files)
_LOADED_DICT_TAG    =   "loaded"
_DATA_DICT_TAG      =   "data"
_FILE_DICT_TAG      =   "files"
_NUM_DICT_TAG       =   "num_frames"

# This function builds a basic frame dictionary for a given list of frames.
def _create_frame_dict(files : list[str]):
    return {
        _LOADED_DICT_TAG    :   False,
        _DATA_DICT_TAG      :   [],
        _FILE_DICT_TAG      :   files,
        _NUM_DICT_TAG       :   len(files)
    }

_gman_images = _create_frame_dict(_GMAN_LST)
_veil_images = _create_frame_dict(_VEIL_LST)
_hawk_images = _create_frame_dict(_HAWK_LST)
_prog_images = _create_frame_dict(_STAMINA_LST)
_back_images = _create_frame_dict(_TMP_BACK_LST)
_warn_images = _create_frame_dict(_TMP_WARN_LST)
_dama_images = _create_frame_dict(_TMP_DMG_LST)
_acti_images = _create_frame_dict(_TMP_ACTIVE_LST)
_heal_images = _create_frame_dict(_HEALTH_LST)
_cemp_images = _create_frame_dict(_NO_CARDS_LST)
_plef_images = _create_frame_dict(_PISTOL_LEFT_LST)
_prig_images = _create_frame_dict(_PISTOL_RIGHT_LST)
_piup_images = _create_frame_dict(_PISTOL_UP_LST)
_pdow_images = _create_frame_dict(_PISTOL_DOWN_LST)
_enhp_images = _create_frame_dict(_ENEMY_HP_LST)

# The data map maps a given frame "tag" to its actual frame dict.
_data_map = {
    TAG_GUARDSMAN   : _gman_images,
    TAG_VEIL        : _veil_images,
    TAG_REVAL_HAWK  : _hawk_images,
    TAG_PROGRESS    : _prog_images,
    TAG_WARN_TEMP   : _warn_images,
    TAG_DAMAGE_TEMP : _dama_images,
    TAG_ACTIVE_TEMP : _acti_images,
    TAG_BACK_TEMP   : _back_images,
    TAG_HEALTH      : _heal_images,
    TAG_CARDS_NONE  : _cemp_images,
    TAG_RIGHT_PISTOL: _prig_images,
    TAG_LEFT_PISTOL : _plef_images,
    TAG_UP_PISTOL   : _piup_images,
    TAG_DOWN_PISTOL : _pdow_images,
    TAG_RIGHT_RIFLE : _prig_images,
    TAG_LEFT_RIFLE  : _plef_images,
    TAG_UP_RIFLE    : _piup_images,
    TAG_DOWN_RIFLE  : _pdow_images,
    TAG_ENEMY_HP    : _enhp_images,
}

# This function loads an image into memory and stores it in the correct spot in the
#   dictionary, if one exists. It returns true of this succeeds.
def _load_images(images : dict):
    if _LOADED_DICT_TAG         not in  images or \
        _DATA_DICT_TAG          not in  images or \
        _FILE_DICT_TAG        not in  images or \
        _NUM_DICT_TAG   not in  images or \
        images[_LOADED_DICT_TAG]:
            return False
    for file in images[_FILE_DICT_TAG]:
        images[_DATA_DICT_TAG] += [cv2.imread(file, cv2.IMREAD_UNCHANGED)]
    images[_LOADED_DICT_TAG]    =   True
    return True
    
# This function removes images from memory. True on success.
def _unload_images(images : dict):
    if  _LOADED_DICT_TAG    not in  images or \
        _DATA_DICT_TAG      not in  images:
        return False
    images[_LOADED_DICT_TAG]    =   False
    images[_DATA_DICT_TAG]      =   []
    return True

# This function gets a list of all frames (as cv2 images) at a given tag.
#   It also returns False on failure and True otherwise.
def get_frame_lst(id : str):
    if id not in _data_map:
        return None, False
    entry = _data_map[id]
    if not entry[_LOADED_DICT_TAG]:
        _load_images(entry)
    return entry[_DATA_DICT_TAG], True

# This function loads a single image dictionary into memory.
def preload_id(id : str):
    if id not in _data_map:
        return False
    return _load_images(_data_map[id])

# This function loads a group of image dictionaries into memory.
def preload_id_lst(ids : list[str]):
    result = True
    for id in ids:
        result = result and preload_id(id)
    return result

# This function unloads a single image dictionary from memory.
def unload_id(id : str):
    if id not in _data_map:
        return False
    return _unload_images(_data_map[id])

# This function unloads a group of image dictionaries from memory.
def unload_id_lst(ids : list[str]):
    result = True
    for id in ids:
        result = result and unload_id(id)
    return result