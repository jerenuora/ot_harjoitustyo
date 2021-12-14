# Tetris

A kind of Tetris written in python with pygame. 

A course project for Software Development Methods in the University of Helsinki. 

## Releases
- [Viikko 5](https://github.com/jerenuora/ot_harjoitustyo/releases/tag/viikko5)
- [Viikko 6](https://github.com/jerenuora/ot_harjoitustyo/releases/tag/viikko6)

## Documentation
- [Worked hours](https://github.com/jerenuora/ot_harjoitustyo/blob/master/dokumentaatio/tuntikirjapinto.md)
- [Requirements specification](https://github.com/jerenuora/ot_harjoitustyo/blob/master/dokumentaatio/Vaatimusmäärittely.md)
- [Architecture](https://github.com/jerenuora/ot_harjoitustyo/blob/master/dokumentaatio/Architecture.md)
## Installation
- Install dependencies with:
```bash
poetry install
```

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
