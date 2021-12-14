# Tetris

A kind of Tetris written in python with pygame. 

A course project for Software Development Methods in the University of Helsinki. 

## Releases
- [Viikko 5](https://github.com/jerenuora/ot_harjoitustyo/releases/tag/viikko5)
- [Viikko 6](https://github.com/jerenuora/ot_harjoitustyo/releases/tag/viikko6)

## Documentation
- [Tuntikirjanpito](https://github.com/jerenuora/ot_harjoitustyo/blob/master/dokumentaatio/tuntikirjapinto.md)
- [Vaatimusmäärittely](https://github.com/jerenuora/ot_harjoitustyo/blob/master/dokumentaatio/Vaatimusmäärittely.md)
- [Arkkitehtuuri](https://github.com/jerenuora/ot_harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
## Installation
- Install dependencies with:
```bash
poetry install
```
## Keys
Play with arrow keys, drop with space. P for pause. 

## Commands
### Run program 
- Run with:
```bash
poetry run invoke start
```

### Testing 
- Run tests with:
```bash 
poetry run invoke test
```

### Test coverage
- Run coverage tests:
```bash 
poetry run invoke coverage
```
- Generate test coverage raport with:
```bash
poetry run invoke coverage-report
```

### Pylint
- Run pylint with:
```bash
poetry run invoke lint
```
