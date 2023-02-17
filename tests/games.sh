#!/bin/bash

# test the route /
curl -s -X GET http://localhost:8000/ 

# test the route /games
curl -s -X GET http://localhost:8000/games 

# test the route /games/:id
curl -s -X GET http://localhost:8000/games/1