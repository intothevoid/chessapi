
#!/bin/bash

# test the route /games with POST with body {"name": "test"}
curl -s -X POST -H "Content-Type: application/json" \
    http://localhost:8000/api/v1/games -d '{"player1": "Vishwanathan", "player2": "Gary", "state": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"}' 

curl -s -X POST -H "Content-Type: application/json" \
    http://localhost:8000/api/v1/games -d '{"player1": "John", "player2": "Wick", "state": "rnbqkb1r/ppppp1pp/5n2/5p2/8/2N2N2/PPPPPPPP/R1BQKB1R w KQkq - 2 3"}' 