import sys
from mediaManager import MediaManager

sys.path.append("webapp")
# class imports
from webapp import WebApp
from mediaItem import MediaItem
from pipeline.mediaBuilder import MediaBuilder


class MediaEventManager:
    request_limit = 10
    request_counter = 0
    mediaManager = MediaManager()

    def start_media_manager():
        MediaEventManager.mediaManager.start()

    def update(media_item: MediaItem):
        MediaEventManager.mediaManager.update(media_item)

    def build_media(new_request_form: dict) -> bool:
        MediaEventManager.request_counter += 1
        if MediaEventManager.request_counter > MediaEventManager.request_limit:
            return False

        try:
            media_item = MediaBuilder(new_request_form)
            MediaEventManager.update(media_item)
            MediaEventManager.request_counter -= 1

        except Exception as e:
            MediaEventManager.request_counter -= 1
            print(f"error processing request{e}")
            return False

        return True
