# Architecture overview

## Structure

The program follows a three layer architecture, and its package structure is: 

![Untitled Diagram drawio-2](https://user-images.githubusercontent.com/70661652/147417042-bdb31c6c-133f-4311-bc04-aff26005fbdc.png)!



Where UI handles drawing the screen, Sprite operations contains the logic and Sprites and Assets contain the data. In this i've placed the Loop and Gamestate in sprite operations, as they should be in there, but time constraints do not allow me to refactor them in there and write all the documents to reflect the change.  


## User interface

User interface of the game consists of a single window, containing the game and all its additional information. The class Loop calls the UI-class DrawDisplay and its different functions or "screens", that are as follows:
- The pause-screen
- The play-screen
- The gameover with no highscore-screen
- The gameover with a new highscore-screen

The different screens all share the gameboard and its current state in the middle, and on the left are displayed the highscores. Thus they are all contained in a single class with just different parts of the screen changing at different times as functions. 

## Logic 

The gameplayloop Loop is mainly in charge of handling the polling of the input and calling the Gamestate and its movement methods etc. via Actions in sprite.operations. Gamestate then performs the calledupon movement, partly by calling the creation and rotation functions in sprite_operations.operations, and partly by performing them in its internal methods. This perhaps leaves the gamestate class to be too big and the movement should have been separated in to its own class, leaving Gamestate to only keep track of the sprites.

## Data storage
Data storage is handled by the database folders's database functions that save and read the SQL-database. Json-loader reads the tetromino-shape instructions needed by creator and rotator.

### Files 
The database uses files configured the [config](https://github.com/jerenuora/ot_harjoitustyo/blob/master/src/config.py) file, that reads them from [.env](https://github.com/jerenuora/ot_harjoitustyo/blob/master/.env), and in the case of testing, [.env.test](https://github.com/jerenuora/ot_harjoitustyo/blob/master/.env.test)

The json file containing the shape instructions set up similarly, and therefore the game could be expanded to contain additional tetromino shapes, for example.  

## Functionality
The following chart shows what happens when the game is started at first. 
![Untitled-2](https://user-images.githubusercontent.com/70661652/144767569-57c16e89-4029-498e-ad60-3ea6f99adc12.png)
![7ebf8f66](https://user-images.githubusercontent.com/70661652/143919758-c6bc3943-8281-49ff-9785-b78bec8c9817.jpg)

## Weaknesses
The class Gamestate is too big, and contains in addition to the state of the game and sprites, the functions to manipulate the sprites, and should have been split up in to smaller classes. 

The UI in general could have been more polished, and it started out very ambitious with its hand drawn graphics, but due to time constraints turned out to be a mix of hand drawn elements and some lines and fonts.  
