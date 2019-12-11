#! /bin/bash
service nginx stop
uwsgi --ini /home/reocar/uwsgi.ini
service nginx start
tail -f /home/reocar/uwsgi.log
