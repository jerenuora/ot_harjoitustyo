# Architecture overview

## Structure

The program follows a three layer architecture, and its package structure is: 

Linkki kuvaan!

Where UI handles drawing the screen, Loop is in charge of the gameplayloop and giving commands to Gamestate, which in turn keeps track of the state of the sprites and hadles manipulating them, using operations found in sprite operations. 


## User interface

User interface of the game consists of a single window, containing the game and all its additional information. The class Loop handles operating the user interface, and only calls the UI-functions to draw the content on the screen. This is an issue that requires some additional thought moving forward. 

## Logic 

The gameplayloop Loop is mainly in charge of handling the polling of the input and calling the Gamestate and its movement methods etc. via Actions in sprite.operations. Gamestate then performs the calledupon movement, partly in its internal funcions and partly in sprite.operations. This should be reworked to be more consistent, possibly by creating a separate class to handle all movement, and leaving Gamestate to only keep track of the sprites. 

![7ebf8f66](https://user-images.githubusercontent.com/70661652/143919758-c6bc3943-8281-49ff-9785-b78bec8c9817.jpg)
![Untitled-2](https://user-images.githubusercontent.com/70661652/144767569-57c16e89-4029-498e-ad60-3ea6f99adc12.png)
