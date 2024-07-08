import asyncio
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
        self.media_processing_queue = []
        self.media_event_file = "media_event_file.txt"
        self.previous_amount_of_items = 0
        self.file_polling_interval = 1

    def add_to_build_queue(self, new_request):

        self.media_processing_queue.append(

        )
