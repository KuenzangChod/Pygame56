# Avoid the Blocks Game

This is a simple game created using the Pygame library in Python. The objective of the game is to control a player character to avoid randomly generated blocks and survive as long as possible.

## Table of Contents

- [Requirements](#requirements)
- [How to Play](#how-to-play)
- [Controls](#controls)
- [Features](#features)
- [Code Explanation](#code-explanation)
- [License](#license)

## Requirements

- Python 3.x
- Pygame library

## How to Play

1. Run the script in a Python environment.
2. Use the left and right arrow keys to move the player character.
3. Avoid the randomly falling blocks.
4. The game will reset if the player collides with a block.

## Controls

- Left Arrow Key: Move player to the left
- Right Arrow Key: Move player to the right

## Features

- Player can move left and right to avoid falling blocks.
- Score is displayed on the screen.
- The game resets when the player collides with a block.

## Code Explanation

- `pygame` library is used for creating the game window and handling events.
- Player and obstacle characteristics are defined.
- Obstacles are randomly generated and fall from the top of the screen.
- Collision detection is implemented to reset the game when the player collides with an obstacle.
- Score is incremented as the game progresses.

## License

This project is licensed under the [MIT License](LICENSE.md).
