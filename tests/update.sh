
#!/bin/bash

# test the route /games/:id with PUT with body {"name": "test"}
curl -s -X PUT http://localhost:8000/api/v1/games/2 -H "Content-Type: application/json" \
    -d '{"player1": "Vishwanathan", "player2": "Gary", "state": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"}' 