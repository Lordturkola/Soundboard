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
    def validate(mediaItem: MediaItem) -> None:
        if mediaItem.video_url == None:
            raise IOError(f"{__class__}, url required")
        if mediaItem.key_bindning == None:
            raise IOError(f"{__class__}, keybinding required")

    def process(mediaItem: MediaItem) -> MediaItem:
        FetchMedia.validate(mediaItem)
        media_folder = os.path.join(MEDIA_DIR, mediaItem.key_bindning)
        if not os.path.exists(media_folder):
            os.mkdir(media_folder)

        filepath = os.path.join(
            media_folder, f"media_file_{mediaItem.key_bindning}.webm"
        )

        mediaItem.file_path = filepath

        options = {
            "download_ranges": utils.download_range_func(
                [], [[mediaItem.start_time, mediaItem.end_time]]
            ),
            "outtmpl": filepath,
            "overwrites": True,
        }
        with YoutubeDL(params=options) as ytdl:
            error_code = ytdl.download(mediaItem.video_url)

        return mediaItem


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
