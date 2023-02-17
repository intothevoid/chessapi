#!/bin/bash

# test the route /games/:id with DELETE
curl -s -X DELETE http://localhost:8000/games/1 