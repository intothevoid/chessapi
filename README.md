# Multiplayer Chess API

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/ChessSet.jpg/500px-ChessSet.jpg" width=80% height=80%></img>

This is a backend service that allows developers to create, read, update, and delete multiplayer chess games. Chess is a popular game that has been around for centuries. Chess is a game that requires strategy and planning. This server could be used to create a chess game, a chess website, or a chess mobile app.

This server has four endpoints that allow developers to create, read, update, and delete multiplayer chess games.

## Routes

### GET /games

This route returns a list of all the games in the database.

#### Example Response

```json
[
    {
        "id": 1,
        "white_player": "John",
        "black_player": "Jane",
        "winner": "John",
        "moves": [
            {
                "id": 1,
                "game_id": 1,
                "move": "e4",
                "player": "John"
            },
            {
                "id": 2,
                "game_id": 1,
                "move": "e5",
                "player": "Jane"
            }
        ]
    },
    {
        "id": 2,
        "white_player": "John",
        "black_player": "Jane",
        "winner": "John",
        "moves": [
            {
                "id": 3,
                "game_id": 2,
                "move": "e4",
                "player": "John"
            },
            {
                "id": 4,
                "game_id": 2,
                "move": "e5",
                "player": "Jane"
            }
        ]
    }
]
```

### POST /games

This route creates a new game in the database.

#### Example Request

```json
{
    "white_player": "John",
    "black_player": "Jane"
}
```

#### Example Response

```json
{
    "id": 1,
    "white_player": "John",
    "black_player": "Jane",
    "winner": null,
    "moves": []
}
```

### GET /games/{game_id}

This route returns a specific game in the database.

#### Example Response

```json
{
    "id": 1,
    "white_player": "John",
    "black_player": "Jane",
    "winner": "John",
    "moves": [
        {
            "id": 1,
            "game_id": 1,
            "move": "e4",
            "player": "John"
        },
        {
            "id": 2,
            "game_id": 1,
            "move": "e5",
            "player": "Jane"
        }
    ]
}
```

### PUT /games/{game_id}

This route updates a specific game in the database.

#### Example Request

```json
{
    "winner": "John"
}
```

#### Example Response

```json
{
    "id": 1,
    "white_player": "John",
    "black_player": "Jane",
    "winner": "John",
    "moves": [
        {
            "id": 1,
            "game_id": 1,
            "move": "e4",
            "player": "John"
        },
        {
            "id": 2,
            "game_id": 1,
            "move": "e5",
            "player": "Jane"
        }
    ]
}
```

### DELETE /games/{game_id}

This route deletes a specific game in the database.

#### Example Response

```json
{
    "id": 1,
    "white_player": "John",
    "black_player": "Jane",
    "winner": "John",
    "moves": [
        {
            "id": 1,
            "game_id": 1,
            "move": "e4",
            "player": "John"
        },
        {
            "id": 2,
            "game_id": 1,
            "move": "e5",
            "player": "Jane"
        }
    ]
}
```

## Setup

### Requirements

- [Python 3.8](https://www.python.org/downloads/release/python-380/)
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