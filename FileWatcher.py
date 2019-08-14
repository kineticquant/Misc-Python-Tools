#MM 08.14.2019

####                       ####      ####                       ####
####  ###             ###  ####      ####  ###             ###  ####
####     ###      ###      ####      ####     ###      ###      ####
####        ## ##          ####      ####        ## ##          ####
####          #            ####      ####          #            ####
####                       ####      ####                       ####
####                       ####      ####                       ####
####                       ####      ####                       ####
####                       ####      ####                       ####

import requests
import re
import urlparse
import netfilterqueue
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    directory = input("Enter the desired path FORMAT(/path/to/my/directory) > ")

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.directory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print "Error"

        self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Action can be taken at this point when a file is created
            print "Host Create Event - %s." % event.src_path

        elif event.event_type == 'modified':
            # Action can be taken at this point when a file is modified
            print "Host Modify Event - %s." % event.src_path

if __name__ == '__main__':
    w = Watcher()
    w.run()
