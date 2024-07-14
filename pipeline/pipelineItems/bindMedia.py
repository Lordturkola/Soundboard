import json
import sys, os
from os.path import dirname

current_dir = os.path.abspath(os.path.curdir)
sys.path.append(os.path.join(current_dir, "model"))
sys.path.append(os.path.join(current_dir, "interfaces"))

from iMediaPipelineItem import IMediaPipelineItem
from mediaItem import MediaItem


class BindMedia(IMediaPipelineItem):
    def validate(mediaItem: MediaItem) -> None:
        if mediaItem.file_path == None:
            raise IOError(f"{__class__}, url required")
        if mediaItem.key_bindning == None:
            raise IOError(f"{__class__}, keybinding required")

    def process(mediaItem: MediaItem) -> MediaItem:
        BindMedia.validate(mediaItem)
        


if __name__ == "__main__":
    mediaItem = FetchMedia.process(
        MediaItem(
            videourl="https://www.youtube.com/watch?v=rJYaKsbExSo&ab_channel=Blue",
            start_time=0.0,
            end_time=3.0,
            file_path=None,
            key_bindning="f",
        )
    )
    print(mediaItem.file_path)
