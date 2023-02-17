from __future__ import annotations

from typing import List, Union

from fastapi import FastAPI

from .models import (
    GamesGameIdGetResponse,
    GamesGameIdPutRequest,
    GamesGetResponse,
    GamesPostRequest,
    GamesPostResponse,
)

app = FastAPI(
    title='Chess Game API',
    version='1.0.0',
    servers=[{'url': 'http://localhost:8000'}],
)


@app.get('/games', response_model=List[GamesGetResponse])
def get_games() -> List[GamesGetResponse]:
    """
    Get a list of all games
    """
    pass


@app.post(
    '/games', response_model=None, responses={'201': {'model': GamesPostResponse}}
)
def post_games(body: GamesPostRequest) -> Union[None, GamesPostResponse]:
    """
    Create a new game
    """
    pass


@app.get('/games/{game_id}', response_model=GamesGameIdGetResponse)
def get_games_game_id(game_id: str) -> GamesGameIdGetResponse:
    """
    Get the details of a game by ID
    """
    pass


@app.put('/games/{game_id}', response_model=None)
def put_games_game_id(game_id: str, body: GamesGameIdPutRequest = ...) -> None:
    """
    Update the state of a game by ID
    """
    pass


@app.delete('/games/{game_id}', response_model=None)
def delete_games_game_id(game_id: str) -> None:
    """
    Delete a game by ID
    """
    pass
