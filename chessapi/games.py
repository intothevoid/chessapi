"""
A chess class representing a chess board
"""
import chess
from dataclasses import dataclass
from typing import Dict


@dataclass
class Game:
    """
    A class to represent a chess game
    """

    def __init__(
        self,
        state: str = None,
        player1: str = "Player 1",
        player2: str = "Player 2",
        id: str = None,  # leave this here for get_copy()
    ):
        # generate a game id
        self.id = self._generate_id()

        # maintain a chess board
        if state is None:
            self.board = chess.Board()
        else:
            self.board = chess.Board(state)

        # player names
        self.player1 = player1
        self.player2 = player2

    def _generate_id(self) -> str:
        """
        Generate a simple incrementing ID for a new game
        """
        # maintain an incrementing ID
        if not hasattr(Game, "id_counter"):
            Game.id_counter = 0
        Game.id_counter += 1

        return str(Game.id_counter)

    def get_copy(self) -> "Game":
        """
        Get a copy of the game
        """
        return Game(
            id=self.id,
            state=self.board.fen(),
            player1=self.player1,
            player2=self.player2,
        )


class Games:
    """
    A class to maintain a list of chess games
    """

    def __init__(self):
        self.games: Dict[str, Game] = {}

    def add_game(
        self,
        state: str = None,
        player1: str = "Player 1",
        player2: str = "Player 2",
    ) -> str:
        """
        Add a new game to the list of games
        """
        game = None
        if state is None:
            game = Game(player1=player1, player2=player2)
        else:
            game = Game(state=state, player1=player1, player2=player2)

        self.games[game.id] = game

        return game.id

    def get_game(self, game_id: str) -> Game:
        """
        Get a game by ID
        """
        if game_id not in self.games:
            raise Exception(f"game with id {game_id} not found")
        return self.games[game_id]

    def update_game(self, game_id: str, state: str) -> None:
        """
        Update a game by ID
        """
        self.games[game_id].board = chess.Board(state)

    def delete_game(self, game_id: str) -> None:
        """
        Delete a game by ID
        """
        temp_copy = None
        if game_id in self.games:
            # make a copy of the game
            temp_copy = self.games[game_id].get_copy()

            # delete the game
            del self.games[game_id]

        return temp_copy

    def get_games(self) -> Dict[str, Game]:
        """
        Get a list of all games
        """
        return self.games

    def get_game_state(self, game_id: str) -> str:
        """
        Get the state of a game by ID
        """
        return self.games[game_id].board.fen()
