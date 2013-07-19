#!/bin/sh

STREAMER=mjpg_streamer
HTTP_PORT=8080

PLUGINPATH=/usr/local/lib

$STREAMER -o "$PLUGINPATH/output_http.so -n -p $HTTP_PORT" -i "$PLUGINPATH/input_raspicam.so -vf -hf -d 80"
