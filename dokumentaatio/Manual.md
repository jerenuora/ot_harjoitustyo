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

The game starts at its “PAUSE” state, so press the “PLAY” button with your mouse, or hit the P-key on your keyboard, to start playing. 

# Keys 

- Move the tetromino with the left-, right-, and down-arrow keys.
- Up-arrow rotatest the tetromino. 
- Spacebar drops the tetromino all the way down. 
- P, or the clickable “PAUSE”-button for pause, and while paused, P, or the clickable “PLAY”-button to resume. 

# Rules

- The tetromino (the gamepiece) moves down, left, or right, until it meets the bottom, or an already fallen tetromino on the bottom. 
- When a row of fallen tetrominoes reaches from one side to the other, it disappears. 
- ##TODO## The game ends when the pile of tetrominoes reaches the top. 
