#!/bin/sh

./streamPiCAM.sh &

python RoombaPi.py

killall mjpg_streamer

