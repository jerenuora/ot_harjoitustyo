# Manual

Download latest [release](https://github.com/jerenuora/ot_harjoitustyo/releases/tag/viikko5)


## Running the program

Before running, install dependencies with:

```bash
poetry install
```

Now run with:

```
poetry run invoke start
```


## Playing the game

The game starts at its “PAUSE” state, so press the “PLAY” button with your mouse, or hit the Enter-key on your keyboard, to start playing. 

# Keys 

- Move the tetromino with the left-, right-, and down-arrow keys.
- Up-arrow rotatest the tetromino. 
- Spacebar drops the tetromino all the way down. 
- Enter, or the clickable “PAUSE”-button for pause, and while paused, Enter, or the clickable “PLAY”-button to resume. 
- You can exit by pressing ESC-key, or just by closing the game-window.
- 
# When the game ends
- If a high score is achieved, enter your initials (3 letters) and press enter.
- If a high score is not achieved, just press enter to play again. 
# Rules

- The tetromino (the gamepiece) moves down, left, or right, until it meets the bottom, or an already fallen tetromino on the bottom. 
- When a row of fallen tetrominoes reaches from one side to the other, it disappears. 
- The game ends when the pile of tetrominoes reaches the top. 
