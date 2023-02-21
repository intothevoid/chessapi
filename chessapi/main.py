from __future__ import annotations

from typing import Dict, List, Optional, Union

from fastapi import FastAPI

from chessapi.models import (
    GamesGameIdDeleteResponse,
    GamesGameIdGetResponse,
    GamesGameIdPutRequest,
    GamesGameIdPutResponse,
    GamesGetResponse,
    GamesPostRequest,
    GamesPostResponse,
)

from chessapi.games import Game, Games
from chessapi import __version__

app = FastAPI(
    title="Chess Game API",
    version=__version__,
    servers=[{"url": "http://localhost:8000"}],
)

ALL_GAMES = Games()


@app.get("/")
def read_root() -> Dict[str, str]:
    try:
        return {
            "API": "Chess API",
            "Description": "A simple chess API.",
            "Version": __version__,
        }
    except Exception as exc:
        return {"error": f"{exc}"}


@app.get("/api/v1/games", response_model=List[GamesGetResponse])
def get_games() -> List[GamesGetResponse] | Dict[str, str]:
    """
    Get a list of all games
    """
    try:
        game_responses = []
        for _, game in ALL_GAMES.get_games().items():
            game_responses.append(
                GamesGetResponse(
                    id=game.id,
                    state=game.board.fen(),
                    player1=game.player1,
                    player2=game.player2,
                )
            )

        return game_responses
    except Exception as exc:
        return {"error": f"{exc}"}


@app.post(
    "/api/v1/games",
    response_model=None,
    responses={"201": {"model": GamesPostResponse}},
)
def post_games(body: GamesPostRequest) -> None | GamesPostResponse:
    """
    Create a new game
    """
    try:
        if body.player1 is None and body.player2 is None:
            return {"error": "must specify at least one player"}
        else:
            # check if any game exists with missing player, if so, add the player to that game
            # else create a new game
            for _, game in ALL_GAMES.get_games().items():
                if not game.player1:
                    game.player1 = body.player1 if body.player1 else body.player2
                    return GamesPostResponse(id=game.id)
                elif not game.player2:
                    game.player2 = body.player1 if body.player1 else body.player2
                    return GamesPostResponse(id=game.id)

            # add the game to the list of games
            id = ALL_GAMES.add_game(body.state, body.player1, body.player2)

        # return the new game's ID
        return GamesPostResponse(id=id)

    except Exception as exc:
        return {"error": f"{exc}"}


@app.get("/api/v1/games/{game_id}", response_model=GamesGameIdGetResponse)
def get_games_game_id(game_id: str) -> GamesGameIdGetResponse | Dict[str, str]:
    """
    Get the details of a game by ID
    """
    try:
        game = ALL_GAMES.get_game(game_id)

        return GamesGameIdGetResponse(
            id=game.id,
            state=game.board.fen(),
            player1=game.player1,
            player2=game.player2,
        )

    except Exception as exc:
        return {"error": f"{exc}"}


@app.put("/api/v1/games/{game_id}", response_model=None)
def put_games_game_id(
    game_id: str, body: GamesGameIdPutRequest = ...
) -> Dict[str, str] | GamesGameIdPutResponse:
    """
    Update the state of a game by ID
    """
    try:
        ALL_GAMES.update_game(game_id, body.state)

        return GamesGameIdPutResponse(id=game_id)

    except Exception as exc:
        return {"error": f"{exc}"}


@app.delete("/api/v1/games/{game_id}", response_model=None)
def delete_games_game_id(game_id: str) -> None | Dict[str, str]:
    """
    Delete a game by ID
    """
    try:
        ALL_GAMES.delete_game(game_id)

        return GamesGameIdDeleteResponse(id=game_id)

    except Exception as exc:
        return {"error": f"{exc}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
