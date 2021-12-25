#Testing

The game has been tested with automated unit- and integrationtests with unittest as well as being manually systemtested.



## Unit- and integrationtestsing 

### Logic
The classes respondible for the game logic, Loop, Gamestate, and Actions are being tested in [TestLoop](https://github.com/jerenuora/ot_harjoitustyo/blob/master/src/tests/loop_test.py), [TestGamestate](https://github.com/jerenuora/ot_harjoitustyo/blob/master/src/tests/gamestate_test.py), [TestActions](https://github.com/jerenuora/ot_harjoitustyo/blob/master/src/tests/gamestate_test.py)

### Database 
The database-classes and functions are tested in [TestDatabase](https://github.com/jerenuora/ot_harjoitustyo/blob/master/src/tests/database_test.py) The tests are being run on test-only files being configured in env.test

### Coverage
Test coverage is at 75% 

<img width="527" alt="Screenshot 2021-12-25 at 19 46 33" src="https://user-images.githubusercontent.com/70661652/147390628-f389887a-bf73-4a41-be7c-a9b2b0c8411b.png">

The coverage is relatively low mostly due to the diffuculty in figuring how and what to test in some of the game logic, like the gameplay loop. 

## Systemtesting
The game has been manually tested by playing it. Also the different UI-elements have been clicked and different inputs have been entered in the scoreboard. 

## Installation and configuration 
The game has been downloaded, installed and tested on macos monterey and linux cubbli, both with latest updates. 

## Functionality 
All of the [requirements specified](https://github.com/jerenuora/ot_harjoitustyo/blob/master/dokumentaatio/Requirements.md) have been met, and some of the additionals too. 
