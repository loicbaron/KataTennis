#!/bin/bash

# backend simulating the games
./katatennis/services/server.py &

# web server
./run.py