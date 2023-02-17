# Multiplayer Chess API

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/ChessSet.jpg/500px-ChessSet.jpg" width=50% height=50%></img>

This is a backend service that allows developers to create, read, update, and delete multiplayer chess games. Chess is a popular game that has been around for centuries. Chess is a game that requires strategy and planning. This server could be used to create a chess game, a chess website, or a chess mobile app.

This server has five endpoints that allow developers to create, read, update, and delete multiplayer chess games.

## Routes

### GET /games

This route returns a list of all the games in the database.

#### Example Response

```json
[
    {
        "id": 1,
        "player1": "John",
        "player2": "Jane",
        "state": "rnbqkbnr/pp1ppppp/8/2p5/8/5N2/PPPPPPPP/RNBQKB1R w KQkq - 0 2"
    },
    {
        "id": 2,
        "player1": "Vishwanathan",
        "player2": "Gary",
        "state": "4k2r/6r1/8/8/8/8/3R4/R3K3 w Qk - 0 1",
    },
]
```

### POST /games

This route creates a new game in the database. An ID is automatically generated for the game. If state is not provided, the game will start with the default chess board.

#### Example Request

```json
{
    "player1": "John",
    "player2": "Jane",
    "state": "rnbqkbnr/pp1ppppp/8/2p5/8/5N2/PPPPPPPP/RNBQKB1R w KQkq - 0 2"
}
```

#### Example Response

```json
{
    "id": 3,
    "player1": "John",
    "player2": "Jane",
    "state": "rnbqkbnr/pp1ppppp/8/2p5/8/5N2/PPPPPPPP/RNBQKB1R w KQkq - 0 2"
}
```

### GET /games/{game_id}

This route returns a specific game in the database.

#### Example Response

```json
{
    "id": 1,
    "player1": "John",
    "player2": "Jane",
    "state": "rnbqkbnr/pp1ppppp/8/2p5/8/5N2/PPPPPPPP/RNBQKB1R w KQkq - 0 2"
}
```

### PUT /games/{game_id}

This route updates a specific game in the database.

#### Example Request

```json
{
    "state": "rnbqkbnr/pp1ppppp/8/2p5/8/5N2/PPPPPPPP/RNBQKB1R w KQkq - 0 2"
}
```

#### Example Response

```json
{
    "id": 1,
}
```

### DELETE /games/{game_id}

This route deletes a specific game in the database.

#### Example Response

```json
{
    "id": 1,
}
```

## Setup

### Requirements

- [Python 3.8](https://www.python.org/downloads/release/python-380/)
- [Python Chess](https://python-chess.readthedocs.io/en/latest/)
- [FastAPI](https://fastapi.tiangolo.com/)

### Installation

1. Clone the repository

```bash
git clone https://github.com/intothevoid/chessapi.git
```

2. Install dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Run the server

```bash
PYTHONPATH=.
uvicorn chessapi.main:app --reload
```

## References

- [Chess](https://en.wikipedia.org/wiki/Chess)
- [FastAPI](https://fastapi.tiangolo.com/)
- [FastAPI Code Generator](https://github.com/koxudaxi/fastapi-code-generator)