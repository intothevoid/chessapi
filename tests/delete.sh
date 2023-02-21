#!/bin/bash

# test the route /games/:id with DELETE
curl -s -X DELETE http://localhost:8000/api/v1/games/1 