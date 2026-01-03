# Python-OpenCV-2D-Game

A simple grid-based game made using Python, OpenCV (CV2 + CVZone), and PlaySound3. The game is very, very loosely based on an old game from the LEGO website (Spinjitzu Smash DX) that I played way too much of as a kid.
There are two player characters (Veil and Guardsman) and one enemy character (Hawk). You select your active player and get three random cards, shown on the top bar. These cards are attacks, and fire your weapon in one of four directions.

Controls:

- w - move up
- a - move left
- s - move down
- d - move right
- q - use card 1
- e - use card 2
- r - use card 3
- 1 - switch to Guardsman
- 2 - switch to Veil
- x - exit

The game is played on a 10x4 grid, where each attack causes entities on certain tiles to take damage. Attacks can only be used when the stamina bar is full; the stamina bar takes 5 seconds to recharge from empty, but not all attacks completely empty it (e.g., switching characters only takes off 1.5 seconds). Self-damage is disabled, but friendly fire isn't.

Here's a quick demo:

https://www.youtube.com/watch?v=Snie2e48h68

This project was made across three days (12/31/25 to 1/2/26), with day 1 being mostly concept work, day 2 being rebuilding the codebase from the ground up, and day 3 being polishing and documentation.
