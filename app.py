#!/usr/bin/python

import time, requests
from flask import Flask
app = Flask(__name__)

START = time.time()

def elapsed():
    running = time.time() - START
    minutes, seconds = divmod(running, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

def update():
    r = requests.post('www.google-analytics.com/collect',
                      data = {'v': 1,
                              'tid': 'UA-57322503-11',
                              'cid': '666',
                              't': 'event',
                              'ec': 'tutorial',
                              'ea': 'start'
                              })

@app.route('/')
def root():
    update()
    return "Hello World! (up %s)\n" % elapsed()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
