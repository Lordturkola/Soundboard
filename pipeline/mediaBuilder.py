from mediaItem import MediaItem
from pipelineItems.fetchMedia import FetchMedia


class MediaBuilder:
    def __init__(self, rawMediaItem):
        self.media_item = self.extract_data(rawMediaItem)
        self.pipeline = [
            FetchMedia,
        ]

    def process(self) -> MediaItem:
        for pipelineItem in self.pipeline:
            self.media_item = pipelineItem.process(self.media_item)
        return self.media_item

    def extract_data(self, rawItem) -> MediaItem:
        return MediaItem(
            video_url=rawItem.get("videoUrl"),
            start_time=int(rawItem.get("startTime")),
            end_time=int(rawItem.get("endTime")),
            key_bindning=rawItem.get("keybinding"),
            file_path=None,
        )
