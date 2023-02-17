# generated by fastapi-codegen:
#   filename:  openapi.yml
#   timestamp: 2023-02-17T03:55:10+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class GamesGetResponse(BaseModel):
    id: Optional[str] = Field(None, description='The unique ID of the game')
    state: Optional[str] = Field(
        None, description="The FEN representation of the game's state"
    )
    player1: Optional[str] = Field(None, description='The name of player 1')
    player2: Optional[str] = Field(None, description='The name of player 2')


class GamesPostRequest(BaseModel):
    state: Optional[str] = Field(
        None, description="The FEN representation of the game's initial state"
    )
    player1: Optional[str] = Field(None, description='The name of player 1')
    player2: Optional[str] = Field(None, description='The name of player 2')


class GamesPostResponse(BaseModel):
    id: Optional[str] = Field(None, description='The unique ID of the new game')


class GamesGameIdGetResponse(BaseModel):
    id: Optional[str] = Field(None, description='The unique ID of the game')
    state: Optional[str] = Field(
        None, description="The FEN representation of the game's state"
    )
    player1: Optional[str] = Field(None, description='The name of player 1')
    player2: Optional[str] = Field(None, description='The name of player 2')


class GamesGameIdPutRequest(BaseModel):
    state: Optional[str] = Field(
        None, description="The FEN representation of the game's new state"
    )