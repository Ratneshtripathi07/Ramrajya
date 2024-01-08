# Ramrajya: Slay The Evil

## Overview

"Ramrajya: Slay The Evil" is a 2D Arrow shooter game developed in Python using the Pygame library. The game is set in a mythological world where the player, assuming the role of Lord Shree Ram, slays the evil 'Danavas' and restores peace to the land.

## Features

- **Player Controls:** Control the character using keyboard inputs (left arrow key, right arrow key, space key).
- **Enemy Entities (Danavas):** Evil demons populate the game world, presenting challenges for the player.
- **Levels:** Multiple levels with increasing difficulty as the score rises.
- **Scoring System:** Earn points for killing demons; progress is tracked through a customizable scoring system.
- **Graphics and Sound:** Pygame is utilized for rendering graphics, and sound effects enhance the gaming experience.

## Installation

1. Ensure you have Python installed on your system.
2. Install the Pygame library using the following command:

    ```bash
    pip install pygame
    ```

3. Clone the game repository:

    ```bash
    git clone https://github.com/Ratneshtripathi07/Ramrajya.git
    ```

4. Navigate to the game directory:

    ```bash
    cd ramrajya
    ```

5. Run the game:

    ```bash
    python Ramrajya.py
    ```

## Controls

- **Arrow Keys:** Move character left or right.
- **Space Bar:** Attack.

## Game Structure

- **Main Menu:** The starting point of the game where players can start a new game or exit.
- **Gameplay:** Navigate through various levels, defeat demons, and reach new high scores.
- **Game Over:** Displays the final score and options to restart or quit.

## Code Structure

- **Ramrajya.py:** Main functionality controls, display initialization.
- **Settings.py:** Game settings such as display resolution, arrows limit, speeds, high score, etc.
- **Kodanda.py:** 'The Bow' is drawn on the screen, and key events governing its position are updated in the main game file (Ramrajya.py).
- **Ramastra.py:** Adds the 'Arrow' on the bow and updates the keypress event for the space key to launch.
- **Danav.py:** Contains details for the demons' number (Sena), arrangement, and movement.
- **Start Button:** Draws a rectangle in the middle of the screen, and the text "Play" is rendered.
- **Gamestats.py:** Stores data like scores, life, etc.
- **Scoreboard.py:** Stores the score and tracks the high score.

## Credits

- Developed by Ratnesh.
- Pygame library: [https://www.pygame.org/](https://www.pygame.org/)

## License

This game is released under the MIT License.
