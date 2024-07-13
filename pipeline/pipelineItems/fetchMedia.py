import json
import sys, os
from os.path import dirname

current_dir = os.path.abspath(os.path.curdir)
sys.path.append(os.path.join(current_dir, "model"))
sys.path.append(os.path.join(current_dir, "interfaces"))

from iMediaPipelineItem import IMediaPipelineItem
from mediaItem import MediaItem
from yt_dlp import YoutubeDL, utils

MEDIA_DIR = os.path.join(dirname(dirname(current_dir)), "media")


class FetchMedia(IMediaPipelineItem):

    def __init__(self, mediaItem: MediaItem) -> None:
        FetchMedia.validate(mediaItem)
        self.mediaItem = mediaItem

    def validate(mediaItem: MediaItem) -> None:
        if mediaItem.video_url == None:
            raise IOError(f"{__class__}, url required")
        if mediaItem.key_bindning == None:
            raise IOError(f"{__class__}, keybinding required")

    def process(self) -> MediaItem:
        media_folder = os.path.join(MEDIA_DIR, self.mediaItem.key_bindning)
        if not os.path.exists(media_folder):
            os.mkdir(media_folder)

        filepath = os.path.join(
            media_folder, f"media_file_{self.mediaItem.key_bindning}.webm"
        )

        self.mediaItem.file_path = filepath

        options = {
            "continuedl": False,
            "download_ranges": utils.download_range_func(
                [], [[self.mediaItem.start_time, self.mediaItem.end_time]]
            ),
            "outtmpl": filepath,
            "overwrites": True,
        }
        with YoutubeDL(params=options) as ytdl:
            error_code = ytdl.download(self.mediaItem.video_url)

        return self.mediaItem


if __name__ == "__main__":
    builditem = FetchMedia(
        MediaItem(
            videourl="https://www.youtube.com/watch?v=rJYaKsbExSo&ab_channel=Blue",
            start_time=0.0,
            end_time=3.0,
            file_path=None,
            key_bindning="f",
        )
    )

    result = builditem.process()
    print(result.file_path)
