from __future__ import annotations

from typing import Dict, List, Union

from fastapi import FastAPI

from .models import (
    GamesGameIdGetResponse,
    GamesGameIdPutRequest,
    GamesGetResponse,
    GamesPostRequest,
    GamesPostResponse,
)

from .games import Game, Games

app = FastAPI(
    title="Chess Game API",
    version="1.0.0",
    servers=[{"url": "http://localhost:8000"}],
)

ALL_GAMES = Games()


@app.get("/games", response_model=List[GamesGetResponse])
def get_games() -> List[GamesGetResponse]:
    """
    Get a list of all games
    """
    return ALL_GAMES.get_games()


@app.post(
    "/games", response_model=None, responses={"201": {"model": GamesPostResponse}}
)
def post_games(body: GamesPostRequest) -> Union[None, GamesPostResponse]:
    """
    Create a new game
    """

    # create a new game
    new_game = Game(state=body.state, player1=body.player1, player2=body.player2)

    # add the game to the list of games
    ALL_GAMES.add_game(new_game)

    # return the new game's ID
    return GamesPostResponse(id=new_game.id)


@app.get("/games/{game_id}", response_model=GamesGameIdGetResponse)
def get_games_game_id(game_id: str) -> GamesGameIdGetResponse:
    """
    Get the details of a game by ID
    """
    game = ALL_GAMES.get_game(game_id)
    return GamesGameIdGetResponse(
        id=game.id,
        state=game.board.fen(),
        player1=game.player1,
        player2=game.player2,
    )


@app.put("/games/{game_id}", response_model=None)
def put_games_game_id(game_id: str, body: GamesGameIdPutRequest = ...) -> None:
    """
    Update the state of a game by ID
    """
    ALL_GAMES.update_game(game_id, body.state)


@app.delete("/games/{game_id}", response_model=None)
def delete_games_game_id(game_id: str) -> None:
    """
    Delete a game by ID
    """
    ALL_GAMES.delete_game(game_id)
