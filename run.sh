#!/bin/bash

export FLASK_APP=$(pwd)/server.py
flask run --host=0.0.0.0