#!/bin/sh


# Seems to work OK and ~10fps
raspistill -vf -hf -t 9999999 -tl 100 -o /tmp/test.jpg -n -w 640 -h 480 &

mjpg_streamer -i "input_file.so -f /tmp -d 0" &

python RoombaPi.py

killall mjpg_streamer
killall raspistill

