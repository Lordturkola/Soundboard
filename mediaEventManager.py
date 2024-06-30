import asyncio
from pathlib import path
from time import sleep

# class imports
from mediaItem import MediaItem


class MediaEventManager:

    def __init__(self) -> None:
        ## workflow
        # event manager recieves an external request
        # gets populated by incoming ssh messages and/or webrequsts
        self.media_processing_queue = []
        self.media_event_file = "media_event_file.txt"
        self.previous_amount_of_items = 0
        self.file_polling_interval = 1

    def start(self):
        # listen to ssh events or web api requests on localhost?
        self.watch_media_request_file()
        pass

    def watch_media_request_file(self):
        while True:
            self.isWatching = True
            with open(self.media_event_file) as file:
                media_items_raw = file.readlines()
                amount_of_items = media_items_raw.length()
                if (
                    amount_of_items > self.previous_amount_of_items
                    and amount_of_items <= 0
                ):
                    new_items = media_items_raw[
                        self.previous_amount_of_items : amount_of_items - 1
                    ]
                    self.add_to_build_queue(new_items)
                    self.previous_amount_of_items = amount_of_items

            sleep(self.file_polling_interval)

    def add_to_build_queue(self, new_items):
        pass
