import sys, os

current_dir = os.path.abspath(os.path.curdir)
sys.path.append(os.path.join(current_dir, "pipeline"))
sys.path.append(os.path.join(current_dir, "pipeline/pipelineItems/model/"))
sys.path.append(os.path.join(current_dir, "pipeline/pipelineItems/interfaces/"))
# class imports
from mediaManager import MediaManager
from mediaItem import MediaItem
from pipeline.mediaBuilder import MediaBuilder
from iMediaPipelineItem import IMediaPipelineItem


class MediaEventManager:
    request_limit = 10
    request_counter = 0
    mediaManager = MediaManager()

    def start_media_manager():
        MediaEventManager.mediaManager.start()

    def update(media_item: MediaItem):
        MediaEventManager.mediaManager.update(media_item)

    def build_media(new_request_form: dict) -> bool:
        print(f"request counter: {MediaEventManager.request_counter}")
        if MediaEventManager.request_counter > MediaEventManager.request_limit:
            print(f"too many requests: {MediaEventManager.request_counter}")
            return False
        try:
            MediaEventManager.request_counter += 1
            media_item = MediaBuilder(new_request_form).process()
            print("updating media manager...")
            MediaEventManager.update(media_item)

        except Exception as e:
            MediaEventManager.request_counter -= 1
            print(f"error processing request{e}")
            return False
        
        MediaEventManager.request_counter -= 1
        return True

    if __name__ == "__main__":
        pass
