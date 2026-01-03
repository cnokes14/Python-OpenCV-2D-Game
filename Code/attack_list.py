from attack import *
from id_list import *

RIGHT_PISTOL = create_attack(
            name = TAG_RIGHT_PISTOL,
            frames=[
                create_attack_frame(10,100,250,1,1,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,TAG_PISTOL_LOAD,TAG_PISTOL_FIRE),
                create_attack_frame(70,100,250,1,2,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(130,100,250,1,3,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(190,100,250,1,4,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(250,100,250,1,5,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
            ],
            cooldown=1500
)

LEFT_PISTOL = create_attack(
            name = TAG_LEFT_PISTOL,
            frames=[
                create_attack_frame(10,100,250,1,-1,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,TAG_PISTOL_LOAD,TAG_PISTOL_FIRE),
                create_attack_frame(70,100,250,1,-2,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(130,100,250,1,-3,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(190,100,250,1,-4,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(250,100,250,1,-5,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
            ],
            cooldown=1500
)

UP_PISTOL = create_attack(
            name = TAG_UP_PISTOL,
            frames=[
                create_attack_frame(10,100,250,1,0,-1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,TAG_PISTOL_LOAD,TAG_PISTOL_FIRE),
                create_attack_frame(70,100,250,1,0,-2,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(130,100,250,1,0,-3,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(190,100,250,1,0,-4,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
            ],
            cooldown=1500
)

DOWN_PISTOL = create_attack(
            name = TAG_DOWN_PISTOL,
            frames=[
                create_attack_frame(10,100,250,1,0,1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,TAG_PISTOL_LOAD,TAG_PISTOL_FIRE),
                create_attack_frame(70,100,250,1,0,2,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(130,100,250,1,0,3,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(190,100,250,1,0,4,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
            ],
            cooldown=1500
)

RIGHT_RIFLE = create_attack(
            name = TAG_RIGHT_RIFLE,
            frames=[
                create_attack_frame(10,500,250,2,1,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,TAG_RIFLE_LOAD,TAG_RIFLE_FIRE),
                create_attack_frame(70,500,250,2,2,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(130,500,250,2,3,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(190,500,250,2,4,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(250,500,250,2,5,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(370,500,250,2,6,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
            ],
            cooldown=5000
)

LEFT_RIFLE = create_attack(
            name = TAG_LEFT_RIFLE,
            frames=[
                create_attack_frame(10,500,250,2,-1,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,TAG_RIFLE_LOAD,TAG_RIFLE_FIRE),
                create_attack_frame(70,500,250,2,-2,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(130,500,250,2,-3,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(190,500,250,2,-4,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(250,500,250,2,-5,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(370,500,250,2,-6,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
            ],
            cooldown=5000
)

DOWN_RIFLE = create_attack(
            name = TAG_DOWN_RIFLE,
            frames=[
                create_attack_frame(10,500,250,2,0,1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,TAG_RIFLE_LOAD,TAG_RIFLE_FIRE),
                create_attack_frame(70,500,250,2,0,2,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(130,500,250,2,0,3,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(190,500,250,2,0,4,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
            ],
            cooldown=5000
)

UP_RIFLE = create_attack(
            name = TAG_UP_RIFLE,
            frames=[
                create_attack_frame(10,500,250,2,0,-1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,TAG_RIFLE_LOAD,TAG_RIFLE_FIRE),
                create_attack_frame(70,500,250,2,0,-2,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(130,500,250,2,0,-3,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(190,500,250,2,0,-4,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
            ],
            cooldown=5000
)

KYETN_DOUBLE_GUN = create_attack(
            name=TAG_HAWK_DOUBLE_GUN,
            frames=[
                create_attack_frame(10,1250,250,1,-1,-1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,TAG_HAWK_DRAW,TAG_HAWK_SLASH_0),
                create_attack_frame(10,1250,250,1,-1,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(10,1250,250,1,-1,1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(70,1250,250,1,-2,-1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,damage_sound=TAG_HAWK_SLASH_1),
                create_attack_frame(70,1250,250,1,-2,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(70,1250,250,1,-2,1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(130,1250,250,1,-3,-1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,damage_sound=TAG_HAWK_SLASH_2),
                create_attack_frame(130,1250,250,1,-3,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(130,1250,250,1,-3,1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(190,1250,250,1,-4,-1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(190,1250,250,1,-4,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(190,1250,250,1,-4,1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
            ],
            cooldown=3500
)

KYETN_DOUBLE_GUN_BACKWARDS = create_attack(
            name=TAG_HAWK_DOUBLE_GUN,
            frames=[
                create_attack_frame(10,1250,250,1,1,-1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,TAG_HAWK_DRAW,TAG_HAWK_SLASH_0),
                create_attack_frame(10,1250,250,1,1,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(10,1250,250,1,1,1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(70,1250,250,1,2,-1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,damage_sound=TAG_HAWK_SLASH_1),
                create_attack_frame(70,1250,250,1,2,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(70,1250,250,1,2,1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(130,1250,250,1,3,-1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,damage_sound=TAG_HAWK_SLASH_2),
                create_attack_frame(130,1250,250,1,3,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(130,1250,250,1,3,1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(190,1250,250,1,4,-1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(190,1250,250,1,4,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(190,1250,250,1,4,1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
            ],
            cooldown=3500
)

KYETN_ZIGZAG = create_attack(
            name=TAG_HAWK_ZIGZAG,
            frames=[
                create_attack_frame(10,1250,250,1,-1,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,TAG_HAWK_DRAW,TAG_HAWK_SLASH_0),
                create_attack_frame(210,1250,250,1,-2,1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(410,1250,250,1,-3,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,damage_sound=TAG_HAWK_SLASH_1),
                create_attack_frame(610,1250,250,1,-4,-1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(810,1250,250,1,-5,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,damage_sound=TAG_HAWK_SLASH_0),
                create_attack_frame(1010,1250,250,1,-6,1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(1210,1250,250,1,-7,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(1410,1250,250,1,-6,-1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(1610,1250,250,1,-5,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,damage_sound=TAG_HAWK_SLASH_0),
                create_attack_frame(1810,1250,250,1,-4,1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(2010,1250,250,1,-3,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,damage_sound=TAG_HAWK_SLASH_1),
                create_attack_frame(2210,1250,250,1,-2,-1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(2410,1250,250,1,-1,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,damage_sound=TAG_HAWK_SLASH_2),
            ],
            cooldown=3500
)

KYETN_ZIGZAG_BACKWARDS = create_attack(
            name=TAG_HAWK_ZIGZAG,
            frames=[
                create_attack_frame(10,1250,250,1,1,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,TAG_HAWK_DRAW,TAG_HAWK_SLASH_0),
                create_attack_frame(210,1250,250,1,2,1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(410,1250,250,1,3,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,damage_sound=TAG_HAWK_SLASH_0),
                create_attack_frame(610,1250,250,1,4,-1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(810,1250,250,1,5,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,damage_sound=TAG_HAWK_SLASH_1),
                create_attack_frame(1010,1250,250,1,6,1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(1210,1250,250,1,7,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(1410,1250,250,1,6,-1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(1610,1250,250,1,5,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,damage_sound=TAG_HAWK_SLASH_0),
                create_attack_frame(1810,1250,250,1,4,1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(2010,1250,250,1,3,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,damage_sound=TAG_HAWK_SLASH_0),
                create_attack_frame(2210,1250,250,1,2,-1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(2410,1250,250,1,1,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,damage_sound=TAG_HAWK_SLASH_2),
            ],
            cooldown=3500
)

KYETN_SLAM = create_attack(
            name=TAG_HAWK_SLAM,
            frames=[
                create_attack_frame(10,1250,250,1,-1,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP,TAG_HAWK_DRAW,TAG_HAWK_SLASH_2),
                create_attack_frame(10,1250,250,1,-1,-1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(10,1250,250,1,-1,1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(10,1250,250,1,0,-1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(10,1250,250,1,0,1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(10,1250,250,1,1,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(10,1250,250,1,1,-1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(10,1250,250,1,1,1,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),

                create_attack_frame(250,1250,250,1,-2,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(250,1250,250,1,-2,-2,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(250,1250,250,1,-2,2,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(250,1250,250,1,0,-2,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(250,1250,250,1,0,2,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(250,1250,250,1,2,0,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(250,1250,250,1,2,-2,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
                create_attack_frame(250,1250,250,1,2,2,TAG_WARN_TEMP,TAG_DAMAGE_TEMP),
            ],
            cooldown=2500
)

# Footsteps are "attacks" triggered on a move, have no impact and occur at the position
#   of the character instantly (or almost instantly) after starting.
GUARDSMAN_FOOTSTEP_0 = create_attack(
    name=TAG_GUARDSMAN_FOOTSTEP_0,
    frames=[
        create_attack_frame(0,200,0,0,0,0,warn_sound=TAG_GUARDSMAN_FOOTSTEP_0),
    ],
    cooldown=0
)
GUARDSMAN_FOOTSTEP_1 = create_attack(
    name=TAG_GUARDSMAN_FOOTSTEP_1,
    frames=[
        create_attack_frame(0,200,0,0,0,0,warn_sound=TAG_GUARDSMAN_FOOTSTEP_1),
    ],
    cooldown=0
)