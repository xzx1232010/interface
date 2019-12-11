#! /bin/bash
service nginx stop
uwsgi --ini /home/xiasan/face/uwsgi.ini
service nginx start
tail -f
