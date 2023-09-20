#!/bin/bash

fileIn=`cat /home/qqbot/axuanWEB/pan/logs/uwsgi.pid`
kill -9 $fileIn

source ~/.bashrc
conda activate webserver
uwsgi -d logs/uwsgi.log config.ini
