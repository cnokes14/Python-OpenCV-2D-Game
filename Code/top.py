from attack_list import *
from player_control import *
from enemy_control import *
from render import *
from sound import *

if __name__ == "__main__":
    # Scene initialization and image pre-loading.
    init_scene(TAG_BACK_TEMP, [
        TAG_GUARDSMAN,
        TAG_VEIL,
        TAG_REVAL_HAWK,
        TAG_PROGRESS,
        TAG_WARN_TEMP,
        TAG_DAMAGE_TEMP,
        TAG_ACTIVE_TEMP,
    ])
    # The first player, a slower but heartier rifleman.
    add_player(name=TAG_GUARDSMAN,
               x=0,
               y=1,
               frame_id=TAG_GUARDSMAN,
               hp=6,
               cards=[
                   RIGHT_RIFLE,
                   RIGHT_RIFLE,
                   LEFT_RIFLE,
                   LEFT_RIFLE,
                   UP_RIFLE,
                   DOWN_RIFLE
                ],
                attributes=[],
                move=300,
                sound_dict={
                    TAG_SOUND_CATEGORY_FOOTSTEPS : [GUARDSMAN_FOOTSTEP_0, GUARDSMAN_FOOTSTEP_1]
                }
    )
    # The second player, a fast and light pistol user.
    add_player(name=TAG_VEIL,
               x=1,
               y=2,
               frame_id=TAG_VEIL,
               hp=4,
               cards=[
                   RIGHT_PISTOL,
                   RIGHT_PISTOL,
                   LEFT_PISTOL,
                   LEFT_PISTOL,
                   UP_PISTOL,
                   DOWN_PISTOL
                ],
                attributes=[],
                move=200,
                sound_dict={
                    TAG_SOUND_CATEGORY_FOOTSTEPS : [GUARDSMAN_FOOTSTEP_0, GUARDSMAN_FOOTSTEP_1]
                }
    )
    # The enemy, a sword wielding robot.
    add_enemy( name=TAG_REVAL_HAWK,
               x=9,
               y=2,
               frame_id=TAG_REVAL_HAWK,
               hp=25,
               attacks=[
                   KYETN_ZIGZAG,
                   KYETN_ZIGZAG_BACKWARDS,
                   KYETN_DOUBLE_GUN,
                   KYETN_DOUBLE_GUN_BACKWARDS,
                   KYETN_SLAM,
                ],
                attributes=[],
                move_min=3000,
                move_max=5000,
                sound_dict={
                    TAG_SOUND_CATEGORY_FOOTSTEPS : [GUARDSMAN_FOOTSTEP_0, GUARDSMAN_FOOTSTEP_1]
                }
    )
    # Background train sounds and music.
    init_background_sounds([
        TAG_TRAIN_BACKGROUND,
        TAG_KALKUTTA_COMBAT_OST,
    ])
    # Loop until we get 'x', the request for an exit.
    command = -1
    while command != 120:
        # At the start of a loop, we get the current time. So, each iteration is one "tick" at time t.
        t = get_time_ms()
        # First, we start any sounds.
        start_sounds(t)
        # Second, we prune any attacks that aren't active anymore (and won't activate in the future)
        prune_expired_attacks_all(t)
        # Third, we allow the enemies to perform actions.
        enemy_actions(t)
        # Forth, if any command was given, perform the player action.
        if command >= 0:
            get_command(chr(command).lower(), t)
        # Fifth, handle all damage that needs to be dealt.
        check_entity_damage_all(t)
        # Sixth, make sure the active player is still alive, and if not, move to the next active player.
        check_active_alive()
        # Seventh, render the newly established scene.
        render(t)
        # Finally, wait up to 1ms for a new command from the user.
        command = cv2.waitKey(1)