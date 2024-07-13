from queue import Queue
from pathlib import path
from time import sleep
import sys 


sys.path.append("webapp")
# class imports
from webapp import WebApp 
from mediaItem import MediaItem
from mediaBuilder import MediaBuilder

class MediaEventManager:

    def __init__(self) -> None:
        ## workflow
        # event manager recieves an external request
        # gets populated by incoming ssh messages and/or webrequsts
        self.media_processing_queue = Queue(100)
        self.previous_amount_of_items = 0   
        self.file_polling_interval = 1

    def add_to_build_queue(self, new_request):
        try:
            self.media_processing_queue.put_nowait(new_request)
        except Queue.full:
            print("Queue is full and cannot receive another request")
